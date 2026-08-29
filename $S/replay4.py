"""Grand replay: all sessions, all recorded file operations, as pure data.

Chronological application of:
  Write tool inputs         -> full file
  cat > heredocs (Bash)     -> full file
  Edit tool inputs          -> old/new replace, guarded by count
  Bash python patches       -> ast-lifted literal replaces, guarded
Never deletes, never executes recorded code.
"""
import ast, json, glob, os, re, sys

REPO = "/Users/tbs/Desktop/DnD"
events = []   # (ts, kind, path, payload)

CAT = re.compile(r"cat\s*(>>?)\s*(?:\"([^\"]+)\"|'([^']+)'|(\S+))\s*<<\s*'(\w+)'\n(.*?)\n\5(?:\n|$)", re.S)
PYBODY = re.compile(r"python3?\s+-\s*<<\s*'(\w+)'\n(.*?)\n\1(?:\n|$)", re.S)

def lit(node):
	try:
		v = ast.literal_eval(node)
		return v if isinstance(v, str) else None
	except Exception: return None

def lift(body):
	try: tree = ast.parse(body)
	except SyntaxError: return []
	path, out = None, []
	for node in ast.walk(tree):
		if isinstance(node, ast.Assign) and len(node.targets) == 1 \
				and isinstance(node.targets[0], ast.Name) and node.targets[0].id in ("p", "path"):
			path = lit(node.value) or path
	for node in ast.walk(tree):
		if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id in ("sub", "patch"):
			if node.func.id == "sub" and len(node.args) >= 2:
				o, n = lit(node.args[0]), lit(node.args[1])
				if o is not None and n is not None: out.append((path, o, n))
			elif len(node.args) >= 2 and isinstance(node.args[1], (ast.List, ast.Tuple)):
				pp = lit(node.args[0])
				for el in node.args[1].elts:
					if isinstance(el, (ast.Tuple, ast.List)) and len(el.elts) >= 2:
						o, n = lit(el.elts[0]), lit(el.elts[1])
						if o is not None and n is not None: out.append((pp, o, n))
		elif isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) \
				and node.func.attr == "replace" and len(node.args) >= 2:
			o, n = lit(node.args[0]), lit(node.args[1])
			if o is not None and n is not None and len(o) > 8: out.append((path, o, n))
	return out

def norm(p):
	if not p: return None
	if not p.startswith("/"): p = os.path.join(REPO, p)
	p = os.path.normpath(p)
	# worktree paths fold back onto the main tree
	p = re.sub(r"/\.claude/worktrees/[^/]+/", "/", p)
	if not p.startswith(REPO + "/"): return None
	rel = os.path.relpath(p, REPO)
	if rel.startswith((".venv", ".git/")) or "scratchpad" in rel: return None
	return p

for tf in glob.glob("/Users/tbs/.claude/projects/-Users-tbs-Desktop-DnD*/*.jsonl"):
	for line in open(tf, encoding="utf-8", errors="replace"):
		try: d = json.loads(line)
		except Exception: continue
		ts = d.get("timestamp", "")
		msg = d.get("message") or {}
		for blk in (msg.get("content") or []) if isinstance(msg.get("content"), list) else []:
			if not (isinstance(blk, dict) and blk.get("type") == "tool_use"): continue
			inp = blk.get("input") or {}
			name = blk.get("name")
			if name == "Write" and inp.get("content") is not None:
				p = norm(inp.get("file_path"))
				if p: events.append((ts, "write", p, inp["content"]))
			elif name == "Edit" and inp.get("old_string") and inp.get("new_string") is not None:
				p = norm(inp.get("file_path"))
				if p: events.append((ts, "edit", p, (inp["old_string"], inp["new_string"], bool(inp.get("replace_all")))))
			elif name == "Bash":
				cmd = inp.get("command") or ""
				for m in CAT.finditer(cmd):
					p = norm(m.group(2) or m.group(3) or m.group(4))
					if p: events.append((ts, "append" if m.group(1) == ">>" else "write", p, m.group(6) + "\n"))
				for m in PYBODY.finditer(cmd):
					for pp, o, n in lift(m.group(2)):
						p = norm(pp)
						if p: events.append((ts, "edit", p, (o, n, False)))

events.sort(key=lambda e: e[0])
print(f"{len(events)} recorded operations across all sessions")

ok = fail = 0
misses = {}
for ts, kind, p, payload in events:
	os.makedirs(os.path.dirname(p), exist_ok=True)
	if kind == "write":
		open(p, "w", encoding="utf-8").write(payload); ok += 1
	elif kind == "append":
		open(p, "a", encoding="utf-8").write(payload); ok += 1
	else:
		old, new, ra = payload
		if not os.path.exists(p):
			fail += 1; misses[p] = misses.get(p, 0) + 1; continue
		s = open(p, encoding="utf-8").read()
		c = s.count(old)
		if c == 0:
			fail += 1; misses[p] = misses.get(p, 0) + 1; continue
		open(p, "w", encoding="utf-8").write(s.replace(old, new) if ra else s.replace(old, new, 1))
		ok += 1
print(f"applied {ok}, failed {fail}")
print("\nfiles with most failed edits (still wrong/missing bases):")
for p, n in sorted(misses.items(), key=lambda x: -x[1])[:15]:
	print(f"  {n:>3}  {os.path.relpath(p, REPO)}")
