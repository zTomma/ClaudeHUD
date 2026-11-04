#!/usr/bin/env python3
"""Base step for scripts/hudanimations_tf.txt: Valve's original with every literal colour turned into a
token (dark mode). tools/hand/patch_anims.py then replaces the hand-designed events."""
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.dirname(HERE))
import migrate as M

def main():
    src = open(os.path.join(ROOT, "#TF2 Files", "scripts", "hudanimations_tf.txt"), encoding="utf-8", errors="replace").read()
    ctx = M.load_ctx()
    count = [0]
    def repl(m):
        var, val = m.group(2), m.group(3)
        v = var.lower()
        cat = "bg" if "bg" in v or "fill" in v else ("img" if "icon" in v or "draw" in v else "fg")
        rgba = M.parse_rgba(val)
        token = M.ROLE_MAP["dark"][cat][M.nearest_role(rgba[:3])]
        count[0] += 1
        return '%s%s\t"%s"\t' % (m.group(1), var, M.with_alpha(token, rgba[3], ctx))
    out = re.sub(r'(Animate\s+\S+\s+)(\S+)\s+"(\d+\s+\d+\s+\d+(?:\s+\d+)?)"[ \t]*', repl, src)
    open(os.path.join(ROOT, "scripts", "hudanimations_tf.txt"), "w", encoding="utf-8", newline="\n").write(
        "// ClaudeHUD: animazioni - colori migrati ai token (DESIGN.md par. 7)\n" + out)
    print("hudanimations: %d literal colours -> tokens" % count[0])

if __name__ == "__main__":
    main()
