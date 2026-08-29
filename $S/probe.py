import json, glob, os
TARGETS = ("GuildKit.py", "FighterKit.py", "ToolsKit.py", "Map_of_Wizard_Training.py",
           "AlignmentKit.py", "Map_of_Titles.py", "WizardKit.py")
hits = []
for tf in glob.glob("/Users/tbs/.claude/projects/-Users-tbs-Desktop-DnD*/*.jsonl"):
	sess = os.path.basename(tf)[:8]
	for line in open(tf, encoding="utf-8", errors="replace"):
		if not any(t in line for t in TARGETS): continue
		try: d = json.loads(line)
		except Exception: continue
		ts = d.get("timestamp", "")[:16]
		msg = d.get("message") or {}
		for blk in (msg.get("content") or []) if isinstance(msg.get("content"), list) else []:
			if isinstance(blk, dict) and blk.get("type") == "tool_use":
				inp = blk.get("input") or {}
				fp = inp.get("file_path") or ""
				if any(fp.endswith(t) for t in TARGETS):
					size = len(inp.get("content") or "") or len(inp.get("new_string") or "")
					hits.append((ts, sess, blk.get("name"), fp.replace("/Users/tbs/Desktop/DnD/", ""), size))
		tr = d.get("toolUseResult")
		if isinstance(tr, dict) and tr.get("originalFile") is not None:
			fp = tr.get("filePath") or ""
			if any(fp.endswith(t) for t in TARGETS):
				hits.append((ts, sess, "EDIT-RESULT(orig)", fp.replace("/Users/tbs/Desktop/DnD/", ""), len(tr["originalFile"])))
hits.sort()
byfile = {}
for ts, sess, tool, fp, size in hits:
	byfile.setdefault(os.path.basename(fp), []).append((ts, sess, tool, fp, size))
for base, rows in sorted(byfile.items()):
	print(f"=== {base}: {len(rows)} tool touches ===")
	for r in rows[:3]: print(f"   first {r[0]} {r[1]} {r[2]:<18} {r[3]} ({r[4]}b)")
	for r in rows[-3:]: print(f"   last  {r[0]} {r[1]} {r[2]:<18} {r[3]} ({r[4]}b)")
