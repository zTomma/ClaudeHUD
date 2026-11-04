"""Helper: take Valve's original .res, migrate it to tokens, then apply hand edits by element path.

edits = { ("Element",): {"key": "value" | ("value", "comment") | None (delete)},
          ("Parent", "Child"): {...} }
Keys ending in _minmode/_lodef/_hidef and [$X360] variants are dropped from edited elements so the
hand geometry is the only one. Adds the hand-written header so tools/migrate.py skips the file.
"""
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.dirname(HERE))
import migrate as M, modes, tokens as T, vdf

DROP = re.compile(r"_(minmode|lodef|hidef)$", re.I)


def lit(role):
    return T.rgba_str(role), "token: " + role


def find_path(nodes, path):
    cur = nodes
    for name in path:
        nxt = None
        for nd in cur:
            if isinstance(nd[1], list) and nd[0].lower() == name.lower():
                nxt = nd[1]
                break
        if nxt is None:
            raise KeyError("element not found: %s" % "/".join(path))
        cur = nxt
    return cur


def patch(rel, edits, header, add=None, remove_blocks=(), optional=False):
    mode = modes.mode_of(rel)
    nodes = vdf.parse(open(os.path.join(ROOT, "#TF2 Files", rel), encoding="utf-8", errors="replace").read())
    M.migrate_nodes(nodes, mode, M.load_ctx())
    root = next(nd[1] for nd in nodes if isinstance(nd[1], list))
    for path, kv in edits.items():
        try:
            body = find_path(root, path)
        except KeyError:
            if optional:
                continue
            raise
        body[:] = [nd for nd in body if not DROP.search(nd[0]) and not (nd[2] and "X360" in nd[2])
                   and not (isinstance(nd[1], list) and nd[0].lower() in remove_blocks)]
        for nd in body:
            if nd[2] and "WIN32" in nd[2]:
                nd[2] = None
        # collapse duplicates created by dropping conditions (keep the first)
        seen = set()
        uniq = []
        for nd in body:
            key = (nd[0].lower(), isinstance(nd[1], list))
            if not isinstance(nd[1], list) and key in seen:
                continue
            seen.add(key)
            uniq.append(nd)
        body[:] = uniq
        for k, v in kv.items():
            if v is None:
                body[:] = [nd for nd in body if nd[0].lower() != k.lower()]
                continue
            val, cm = v if isinstance(v, tuple) else (v, None)
            hit = False
            for nd in body:
                if nd[0].lower() == k.lower() and not isinstance(nd[1], list):
                    nd[1], nd[3], hit = val, cm, True
            if not hit:
                body.append([k, val, None, cm])
    for parent, block_text in (add or []):
        target = find_path(root, parent) if parent else root
        target.extend(vdf.parse(block_text))
    out = "".join("// " + l + "\n" for l in header.strip().split("\n")) + vdf.dump(nodes) + "\n"
    assert "ClaudeHUD: riscritto" in out[:400]
    vdf.parse(out)
    open(os.path.join(ROOT, rel), "w", encoding="utf-8", newline="\n").write(out)
    return out
