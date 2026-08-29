"""Replay the mega-session's file-building Bash commands in order.

Only three shapes are replayed, all with the repo as cwd:
  - cat > <repo file> <<'TAG' heredocs           (creations; deterministic)
  - python heredocs that io.open(...,"w")        (patches; assert-guarded)
  - cp/mv of repo files whose target is missing  (structure moves)
Everything else (tests, greps, servers) is skipped.
"""
import json, os, re, subprocess, sys

T = "/Users/tbs/.claude/projects/-Users-tbs-Desktop-DnD/f8071d5d-95c6-493d-bd1f-17c5c720e5a2.jsonl"
REPO = "/Users/tbs/Desktop/DnD"
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
print(f"{len(cmds)} bash commands in session, chronological")

def is_writer(cmd):
	if re.search(r"cat\s*>\s*(?:'[^']*'|\"[^\"]*\"|\S+)\s*<<", cmd) and "scratchpad" not in cmd.split("<<")[0]:
		return "cat"
	if "python3 - <<" in cmd or "python3 <<" in cmd:
		body = cmd
		if "io.open(" in body and '"w"' in body and "os.remove" not in body and "shutil" not in body:
			return "patch"
	return None

ran = failed = skipped = 0
log = []
for ts, cmd in cmds:
	kind = is_writer(cmd)
	if not kind: skipped += 1; continue
	# strip leading cd lines pointing at the repo; run with cwd=REPO
	r = subprocess.run(["/bin/zsh", "-c", cmd], cwd=REPO, capture_output=True, text=True, timeout=120)
	out = (r.stdout + r.stderr).strip()
	ok = r.returncode == 0 and "AssertionError" not in out and "Traceback" not in out
	tag = "ok " if ok else "FAIL"
	ran += 1; failed += 0 if ok else 1
	# name the files it touched for the log
	files = set(re.findall(r'"((?:Atlas|Documenta|app|Minion)[^"\n]*?\.(?:py|md|js|css|html))"', cmd))
	files |= set(re.findall(r"cat\s*>\s*(\S+?)\s*<<", cmd))
	log.append(f"{tag} {ts[:19]}  {', '.join(sorted(files))[:90] or cmd[:60]!r}")
	if not ok:
		log.append(f"      | {out.splitlines()[-1][:120] if out else '(no output)'}")
print(f"replayed {ran} writers ({failed} failed asserts/errors), skipped {skipped} non-writers\n")
open(sys.argv[1], "w").write("\n".join(log))
print("\n".join(log[-40:]))
