"""Replay the session's recorded file edits — no shell, no deletions.

Two shapes, applied chronologically:
  cat > <repo file> <<'TAG' ... TAG   -> parsed, file written directly
  python3 - <<'TAG' bodies that patch  -> exec'd in-process (they carry their
  files via io.open(..., "w")             own assert guards, so a wrong base
                                          fails loudly instead of corrupting)
"""
import io, json, os, re, sys, contextlib

T = "/Users/tbs/.claude/projects/-Users-tbs-Desktop-DnD/f8071d5d-95c6-493d-bd1f-17c5c720e5a2.jsonl"
REPO = "/Users/tbs/Desktop/DnD"
os.chdir(REPO)

cmds = []
for line in open(T, encoding="utf-8", errors="replace"):
	if '"Bash"' not in line: continue
	try: d = json.loads(line)
	except Exception: continue
	msg = d.get("message") or {}
	for blk in (msg.get("content") or []) if isinstance(msg.get("content"), list) else []:
		if isinstance(blk, dict) and blk.get("type") == "tool_use" and blk.get("name") == "Bash":
			cmds.append((d.get("timestamp", ""), (blk.get("input") or {}).get("command") or ""))
cmds.sort(key=lambda x: x[0])

CAT = re.compile(r"cat\s*>\s*(?:\"([^\"]+)\"|'([^']+)'|(\S+))\s*<<\s*'(\w+)'\n(.*?)\n\4(?:\n|$)", re.S)
PYBODY = re.compile(r"python3?\s+-\s*<<\s*'(\w+)'\n(.*?)\n\1(?:\n|$)", re.S)

applied = failed = created = 0
log = []
for ts, cmd in cmds:
	for m in CAT.finditer(cmd):
		path = m.group(1) or m.group(2) or m.group(3)
		if path.startswith("/") and not path.startswith(REPO): continue
		if "scratchpad" in path or "/tmp/" in path: continue
		rel = os.path.relpath(os.path.join(REPO, path) if not path.startswith("/") else path, REPO)
		if rel.startswith(".."): continue
		full = os.path.join(REPO, rel)
		os.makedirs(os.path.dirname(full), exist_ok=True)
		body = m.group(5) + "\n"
		mode = "a" if re.search(r"cat\s*>>", cmd[:m.start()+8]) else "w"
		with open(full, mode, encoding="utf-8") as f: f.write(body)
		created += 1
		log.append(f"cat  {ts[:19]}  {rel} ({len(body)}b)")
	for m in PYBODY.finditer(cmd):
		body = m.group(2)
		if "io.open(" not in body or '"w"' not in body: continue
		if "scratchpad" in body or "os.remove" in body or "shutil" in body: continue
		buf = io.StringIO()
		try:
			with contextlib.redirect_stdout(buf):
				exec(compile(body, "<patch>", "exec"), {"__name__": "__patch__"})
			applied += 1
			log.append(f"ok   {ts[:19]}  {buf.getvalue().strip().splitlines()[0][:96] if buf.getvalue().strip() else '(patch)'}")
		except Exception as e:
			failed += 1
			log.append(f"FAIL {ts[:19]}  {type(e).__name__}: {str(e)[:90]}")

open(sys.argv[1], "w").write("\n".join(log))
print(f"heredoc files written: {created}   patches applied: {applied}   patches failed: {failed}")
print("\nlast 30 log lines:")
print("\n".join(log[-30:]))
