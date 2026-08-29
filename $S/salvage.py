"""Scan every session transcript; keep, per file, the latest full-content view."""
import json, os, glob, sys

TDIR = "/Users/tbs/.claude/projects/-Users-tbs-Desktop-DnD"
REPO = "/Users/tbs/Desktop/DnD"
latest = {}   # path -> (timestamp, kind, content)

def offer(path, ts, kind, content):
	if not path or not path.startswith(REPO) or content is None: return
	if isinstance(content, list): return
	cur = latest.get(path)
	if cur is None or ts >= cur[0]:
		latest[path] = (ts, kind, content)

for tf in glob.glob(TDIR + "/*.jsonl"):
	sess = os.path.basename(tf)[:8]
	for line in open(tf, encoding="utf-8", errors="replace"):
		try: d = json.loads(line)
		except Exception: continue
		ts = d.get("timestamp", "")
		# 1) Write tool calls: full content in the request itself
		msg = d.get("message") or {}
		for blk in (msg.get("content") or []) if isinstance(msg.get("content"), list) else []:
			if isinstance(blk, dict) and blk.get("type") == "tool_use":
				inp = blk.get("input") or {}
				if blk.get("name") == "Write":
					offer(inp.get("file_path"), ts, f"write:{sess}", inp.get("content"))
		# 2) toolUseResult: Edits carry originalFile; Reads carry file.content
		tr = d.get("toolUseResult")
		if isinstance(tr, dict):
			fp = tr.get("filePath") or (tr.get("file") or {}).get("filePath")
			if tr.get("originalFile") is not None and fp:
				# apply the edit to the pre-image so we get the post-state
				orig, old, new = tr["originalFile"], tr.get("oldString"), tr.get("newString")
				if old is not None and new is not None and old in orig:
					body = orig.replace(old, new) if tr.get("replaceAll") else orig.replace(old, new, 1)
				else:
					body = orig
				offer(fp, ts, f"edit:{sess}", body)
			f = tr.get("file")
			if isinstance(f, dict) and f.get("content") is not None:
				offer(f.get("filePath"), ts, f"read:{sess}", f["content"])

print(f"{len(latest)} files with recoverable full content\n")
missing, reverted, ok = [], [], 0
for path, (ts, kind, content) in sorted(latest.items()):
	rel = os.path.relpath(path, REPO)
	if rel.startswith((".venv", ".git")): continue
	if not os.path.exists(path):
		missing.append((rel, ts, kind, len(content)))
	else:
		disk = open(path, encoding="utf-8", errors="replace").read()
		if disk.strip() == content.strip(): ok += 1
		else: reverted.append((rel, ts, kind, len(content), len(disk)))
print(f"=== GONE from disk, recoverable: {len(missing)} ===")
for rel, ts, kind, n in missing[:45]: print(f"  {rel}   ({kind} {ts[:10]}, {n}b)")
if len(missing) > 45: print(f"  ... +{len(missing)-45} more")
print(f"\n=== PRESENT but DIFFERENT (transcript is newer or older): {len(reverted)} ===")
for rel, ts, kind, n, dn in reverted[:35]: print(f"  {rel}   (transcript {n}b vs disk {dn}b, {kind} {ts[:10]})")
if len(reverted) > 35: print(f"  ... +{len(reverted)-35} more")
print(f"\n=== already identical on disk: {ok} ===")
json.dump({p: {"ts": t, "kind": k, "content": c} for p, (t, k, c) in latest.items()},
          open(sys.argv[1], "w"))
