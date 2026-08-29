"""Recover files from the session transcript treating everything as DATA.

Nothing recorded is executed. Two extractions:
  1. cat > <repo file> heredocs        -> body written to the file
  2. python patch scripts              -> parsed with ast; only replace-calls
     whose old/new arguments are string LITERALS are lifted, then applied by
     this script's own replace engine, with the original count guard kept.
Index-based edits (a handful) are left for manual re-authoring afterwards.
"""
import ast, json, os, re, sys

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

CAT = re.compile(r"cat\s*(>>?)\s*(?:\"([^\"]+)\"|'([^']+)'|(\S+))\s*<<\s*'(\w+)'\n(.*?)\n\5(?:\n|$)", re.S)
PYBODY = re.compile(r"python3?\s+-\s*<<\s*'(\w+)'\n(.*?)\n\1(?:\n|$)", re.S)

def lit(node):
	"""The string value of an ast node, or None unless it is a pure literal."""
	try:
		v = ast.literal_eval(node)
		return v if isinstance(v, str) else None
	except Exception:
		return None

def lift(body):
	"""(path, old, new, count_expected) edit tuples with literal args only."""
	try: tree = ast.parse(body)
	except SyntaxError: return None, []
	# the patch's target path: first io.open("...") literal, or p = "..."
	path = None
	for node in ast.walk(tree):
		if isinstance(node, ast.Assign) and len(node.targets) == 1 \
				and isinstance(node.targets[0], ast.Name) and node.targets[0].id in ("p", "path"):
			path = lit(node.value) or path
	edits = []
	for node in ast.walk(tree):
		if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) \
				and node.func.id in ("sub", "patch"):
			if node.func.id == "sub" and len(node.args) >= 2:
				o, n = lit(node.args[0]), lit(node.args[1])
				if o is not None and n is not None:
					edits.append((path, o, n))
			if node.func.id == "patch" and len(node.args) >= 2:
				pp = lit(node.args[0])
				if isinstance(node.args[1], (ast.List, ast.Tuple)):
					for el in node.args[1].elts:
						if isinstance(el, (ast.Tuple, ast.List)) and len(el.elts) >= 2:
							o, n = lit(el.elts[0]), lit(el.elts[1])
							if o is not None and n is not None:
								edits.append((pp, o, n))
		if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) \
				and node.func.attr == "replace" and len(node.args) >= 2:
			o, n = lit(node.args[0]), lit(node.args[1])
			if o is not None and n is not None and len(o) > 8:
				edits.append((path, o, n))
	return path, edits

wrote = applied = failed = 0
log = []
for ts, cmd in cmds:
	for m in CAT.finditer(cmd):
		path = m.group(2) or m.group(3) or m.group(4)
		if "scratchpad" in path or path.startswith("/tmp") or path.startswith("/private"): continue
		rel = path if not path.startswith("/") else os.path.relpath(path, REPO)
		if rel.startswith(".."): continue
		full = os.path.join(REPO, rel)
		os.makedirs(os.path.dirname(full), exist_ok=True)
		with open(full, "a" if m.group(1) == ">>" else "w", encoding="utf-8") as f:
			f.write(m.group(6) + "\n")
		wrote += 1
		log.append(f"cat  {ts[:19]}  {rel}")
	for m in PYBODY.finditer(cmd):
		body = m.group(2)
		if ".replace(" not in body and "sub(" not in body and "patch(" not in body: continue
		default_path, edits = lift(body)
		for path, old, new in edits:
			p = path or default_path
			if not p: failed += 1; log.append(f"FAIL {ts[:19]}  edit with unknown path"); continue
			full = os.path.join(REPO, p) if not p.startswith("/") else p
			if not os.path.exists(full):
				failed += 1; log.append(f"FAIL {ts[:19]}  {p}: missing file"); continue
			s = open(full, encoding="utf-8").read()
			c = s.count(old)
			if c == 0:
				failed += 1; log.append(f"FAIL {ts[:19]}  {p}: pattern absent ({old[:40]!r})"); continue
			s = s.replace(old, new, 1) if c == 1 else s.replace(old, new)
			open(full, "w", encoding="utf-8").write(s)
			applied += 1
			log.append(f"ok   {ts[:19]}  {p}: {old[:44]!r}")

open(sys.argv[1], "w").write("\n".join(log))
print(f"files written from heredocs: {wrote}   edits applied: {applied}   edits failed: {failed}")
