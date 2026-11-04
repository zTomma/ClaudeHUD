"""
Tolerant Valve KeyValues (VDF / .res) tokenizer + parser used by every ClaudeHUD tool.

Node = [key, value, cond, comment]
  key     str
  value   str (leaf) or list[Node] (block)
  cond    str or None   e.g. "[$WIN32]"
  comment str or None   trailing // comment on the same line (leaf only)
Top level may also contain ("#base", path) directives, kept as Node(["#base", path, None, None]).
"""
import re

_TOKEN = re.compile(r'''
    (?P<ws>[ \t\r\f\v]+) |
    (?P<nl>\n) |
    (?P<comment>//[^\n]*) |
    (?P<lbrace>\{) |
    (?P<rbrace>\}) |
    (?P<cond>\[[^\]\n]*\]) |
    (?P<qstr>"(?:[^"\\\n]|\\.)*") |
    (?P<badq>"[^\n]*) |
    (?P<word>[^\s{}"\[\]]+)
''', re.X)


class VDFError(Exception):
    pass


def tokenize(text):
    line = 1
    for m in _TOKEN.finditer(text):
        kind = m.lastgroup
        val = m.group()
        if kind == "nl":
            line += 1
            yield ("nl", None, line - 1)
            continue
        if kind == "ws":
            continue
        if kind == "badq":
            raise VDFError("line %d: unterminated quoted string" % line)
        if kind == "qstr":
            yield ("str", val[1:-1], line)
        elif kind == "word":
            yield ("str", val, line)
        else:
            yield (kind, val, line)


def parse(text):
    """Return list of nodes. Raises VDFError with a line number on structural errors."""
    toks = list(tokenize(text))
    pos = 0
    n = len(toks)

    def skip_nl(p):
        while p < n and toks[p][0] in ("nl",):
            p += 1
        return p

    def block(p, depth):
        nodes = []
        while True:
            # skip blank lines and full-line comments
            while p < n and toks[p][0] in ("nl", "comment"):
                p += 1
            if p >= n:
                if depth:
                    raise VDFError("unexpected end of file: %d unclosed '{'" % depth)
                return nodes, p
            kind, val, line = toks[p]
            if kind == "rbrace":
                if not depth:
                    raise VDFError("line %d: unmatched '}'" % line)
                return nodes, p + 1
            if kind != "str":
                raise VDFError("line %d: expected key, got %r" % (line, val))
            key = val
            p += 1
            if key.lower() in ("#base", "#include"):
                if p < n and toks[p][0] == "str":
                    nodes.append(["#base", toks[p][1], None, None])
                    p += 1
                    continue
                raise VDFError("line %d: #base without path" % line)
            # value can be on the same line or a block possibly after newlines/comments
            q = p
            while q < n and toks[q][0] in ("nl", "comment"):
                q += 1
            if q < n and toks[q][0] == "cond":
                r = q + 1
                while r < n and toks[r][0] in ("nl", "comment"):
                    r += 1
                if r < n and toks[r][0] == "lbrace":
                    cond = toks[q][1]
                    children, p = block(r + 1, depth + 1)
                    nodes.append([key, children, cond, None])
                    continue
            if q < n and toks[q][0] == "lbrace":
                children, p = block(q + 1, depth + 1)
                nodes.append([key, children, None, None])
                continue
            if p < n and toks[p][0] == "str":
                value = toks[p][1]
                p += 1
                cond = None
                comment = None
                if p < n and toks[p][0] == "cond":
                    cond = toks[p][1]
                    p += 1
                if p < n and toks[p][0] == "comment":
                    comment = toks[p][1][2:].strip()
                    p += 1
                nodes.append([key, value, cond, comment])
                continue
            raise VDFError("line %d: key %r has no value" % (line, key))

    nodes, _ = block(0, 0)
    return nodes


def _q(s):
    return '"%s"' % s


def dump(nodes, indent=0, align=True):
    out = []
    pad = "\t" * indent
    leaf_keys = [len(_q(k)) for k, v, c, cm in nodes if not isinstance(v, list) and k != "#base"]
    width = max(leaf_keys) if (leaf_keys and align) else 0
    for key, value, cond, comment in nodes:
        if key == "#base":
            out.append('%s#base "%s"' % (pad, value))
            continue
        if isinstance(value, list):
            out.append("%s%s%s" % (pad, _q(key), (" " + cond) if cond else ""))
            out.append("%s{" % pad)
            out.append(dump(value, indent + 1, align))
            out.append("%s}" % pad)
        else:
            k = _q(key)
            gap = "\t" if not width else " " * (width - len(k) + 1) + "\t"
            line = "%s%s%s%s" % (pad, k, gap, _q(value))
            if cond:
                line += " " + cond
            if comment:
                line += "\t// " + comment
            out.append(line)
    return "\n".join(x for x in out if x != "")


def find(nodes, key):
    kl = key.lower()
    for nd in nodes:
        if nd[0].lower() == kl:
            return nd
    return None


def get(nodes, key, default=None):
    nd = find(nodes, key)
    return nd[1] if nd is not None else default


def set_value(nodes, key, value, comment=None):
    """Set every unconditional occurrence of key (or append)."""
    kl = key.lower()
    hit = False
    for nd in nodes:
        if nd[0].lower() == kl and not isinstance(nd[1], list):
            nd[1] = value
            if comment is not None:
                nd[3] = comment
            hit = True
    if not hit:
        nodes.append([key, value, None, comment])


def walk(nodes, path=()):
    """Yield (path, node) for every node, depth-first."""
    for nd in nodes:
        yield path, nd
        if isinstance(nd[1], list):
            yield from walk(nd[1], path + (nd[0],))
