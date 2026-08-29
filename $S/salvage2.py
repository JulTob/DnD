"""Phase 1: restore GONE files from the best transcript snapshot.

Source ranking: Write input == Edit(originalFile+patch)  >  Bash cat-heredoc
>  Read (only when nothing else exists, and flagged UNSURE since Reads can be
partial slices)."""
import json, os, glob, re, sys

TDIR = "/Users/tbs/.claude/projects/-Users-tbs-Desktop-DnD"
REPO = "/Users/tbs/Desktop/DnD"
RANK = {"write": 3, "edit": 3, "bash": 2, "read": 1}
best = {}   # path -> (rank, ts, kind, content)

def offer(path, ts, kind, content):
	if not path or content is None or isinstance(content, list): return
	path = os.path.normpath(path)
	if not path.startswith(REPO + "/"): return
	rank = RANK[kind.split(":")[0]]
	cur = best.get(path)
	# newer beats older at the same rank; higher rank beats lower unless older by a lot? keep simple: rank first, then time
	if cur is None or (rank, ts) >= (cur[0], cur[1]):
		best[path] = (rank, ts, kind, content)

HEREDOC = re.compile(r"cat\s*>\s*(?:\"([^\"]+)\"|'([^']+)'|(\S+))\s*<<\s*'(\w+)'\n(.*?)\n\4\n", re.S)

for tf in sorted(glob.glob(TDIR + "/*.jsonl")):
	sess = os.path.basename(tf)[:8]
	for line in open(tf, encoding="utf-8", errors="replace"):
		try: d = json.loads(line)
		except Exception: continue
		ts = d.get("timestamp", "")
		msg = d.get("message") or {}
		blocks = msg.get("content") if isinstance(msg.get("content"), list) else []
		for blk in blocks:
			if not (isinstance(blk, dict) and blk.get("type") == "tool_use"): continue
			inp = blk.get("input") or {}
			if blk.get("name") == "Write":
				offer(inp.get("file_path"), ts, f"write:{sess}", inp.get("content"))
			elif blk.get("name") == "Bash":
				cmd = inp.get("command") or ""
				for m in HEREDOC.finditer(cmd):
					p = m.group(1) or m.group(2) or m.group(3)
					if p and not p.startswith("/"):
						p = os.path.join(REPO, p)   # cd REPO precedes in our habit
					offer(p, ts, f"bash:{sess}", m.group(5) + "\n")
		tr = d.get("toolUseResult")
		if isinstance(tr, dict):
			fp = tr.get("filePath") or (tr.get("file") or {}).get("filePath")
			if tr.get("originalFile") is not None and fp:
				orig, old, new = tr["originalFile"], tr.get("oldString"), tr.get("newString")
				if old is not None and new is not None and old in orig:
					body = orig.replace(old, new) if tr.get("replaceAll") else orig.replace(old, new, 1)
				else: body = orig
				offer(fp, ts, f"edit:{sess}", body)
			f = tr.get("file")
			if isinstance(f, dict) and f.get("content") is not None:
				offer(f.get("filePath"), ts, f"read:{sess}", f["content"])

restored, unsure, skipped = [], [], 0
for path, (rank, ts, kind, content) in sorted(best.items()):
	rel = os.path.relpath(path, REPO)
	if rel.startswith((".venv", ".git/")) or "/__pycache__/" in rel: continue
	if os.path.exists(path): skipped += 1; continue
	os.makedirs(os.path.dirname(path), exist_ok=True)
	with open(path, "w", encoding="utf-8") as f: f.write(content)
	(unsure if rank == 1 else restored).append((rel, kind, ts[:10], len(content)))

print(f"=== RESTORED with confidence (write/edit/bash): {len(restored)} ===")
for r in restored: print(f"  {r[0]}  ({r[1]} {r[2]}, {r[3]}b)")
print(f"\n=== RESTORED from Read snapshots (may be partial slices, VERIFY): {len(unsure)} ===")
for r in unsure: print(f"  {r[0]}  ({r[1]} {r[2]}, {r[3]}b)")
print(f"\n(still on disk, untouched: {skipped})")
