#!/usr/bin/env python3
"""
Generate the coverage checklist (DESIGN.md §10) for every .res file of the HUD.

Status
  riscritto  hand-written for ClaudeHUD (new layout + tokens)            [x]
  migrato    original layout, every colour/font/border re-pointed to tokens, lint-clean   [~]
  generato   scheme file generated from tools/tokens.py                   [x]
  da fare    still contains default styling or lint errors               [ ]
The reference folders (#TF2 Files, #HL2 Files, #Platform Files, #Map Files) are not loaded
by the game (their paths never match a game path): they are summarised, not listed.

  python3 tools/coverage.py            rewrite the block between the markers in DESIGN.md
  python3 tools/coverage.py --print    print only
"""
import glob
import os
import sys
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import lint as L  # noqa: E402
import migrate as M  # noqa: E402
import modes  # noqa: E402

BEGIN = "<!-- COVERAGE:BEGIN (generato da tools/coverage.py, non modificare a mano) -->"
END = "<!-- COVERAGE:END -->"
GENERATED = {"resource/clientscheme.res", "resource/sourcescheme.res", "resource/chatscheme.res"}


def status_of(rel, names, known):
    text = open(os.path.join(ROOT, rel), encoding="utf-8", errors="replace").read()
    if rel in GENERATED:
        return "generato"
    errors, warnings = [], []
    hand = M.HAND_MARK in text[:400]
    if rel != "resource/pdacontrolpanelscheme.res":
        L.lint_res(rel, text, names, known, hand, errors, warnings)
    if errors:
        return "da fare"
    if hand:
        return "riscritto"
    if "ClaudeHUD: migrato" in text[:200] or rel == "resource/pdacontrolpanelscheme.res":
        return "migrato"
    return "da fare"


def build():
    names = L.scheme_names()
    known = L.corpus()
    files = sorted(os.path.relpath(p, ROOT).replace("\\", "/") for p in
                   glob.glob(os.path.join(ROOT, "resource", "**", "*.res"), recursive=True) +
                   glob.glob(os.path.join(ROOT, "scripts", "**", "*.res"), recursive=True))
    rows = defaultdict(list)
    count = Counter()
    for rel in files:
        st = status_of(rel, names, known)
        count[st] += 1
        rows[os.path.dirname(rel)].append((os.path.basename(rel), modes.mode_of(rel), st))
    mark = {"riscritto": "[x]", "generato": "[x]", "migrato": "[~]", "da fare": "[ ]"}
    out = [BEGIN, "",
           "Legenda: `[x]` riscritto a mano o generato dai token · `[~]` layout originale, stile interamente migrato ai token · `[ ]` da fare.",
           "",
           "**Totale %d file .res** — riscritti %d · generati %d · migrati %d · da fare %d." % (
               len(files), count["riscritto"], count["generato"], count["migrato"], count["da fare"]), ""]
    for d in sorted(rows):
        items = rows[d]
        c = Counter(st for _, _, st in items)
        out.append("<details><summary><code>%s/</code> — %d file (%s)</summary>" % (
            d, len(items), ", ".join("%s %d" % (k, v) for k, v in sorted(c.items()))))
        out.append("")
        out.append("| Stato | File | Modalità |")
        out.append("|:-:|---|---|")
        for fn, mode, st in items:
            out.append("| %s | `%s` | %s |" % (mark[st], fn, {"dark": "scura", "light": "chiara"}.get(mode, mode)))
        out.append("")
        out.append("</details>")
        out.append("")
    ref = Counter()
    for root in ("#TF2 Files", "#HL2 Files", "#Platform Files", "#Map Files"):
        ref[root] = len(glob.glob(os.path.join(ROOT, root, "**", "*.res"), recursive=True))
    out.append("**Cartelle di riferimento** (non caricate dal gioco: i loro percorsi non coincidono con nessun percorso del gioco): " +
               ", ".join("`%s/` %d .res" % (k, v) for k, v in ref.items()) + ". Restano invariate come sorgente degli originali usata da `tools/migrate.py`.")
    out.append("")
    out.append(END)
    return "\n".join(out), count


def main():
    block, count = build()
    if "--print" in sys.argv:
        print(block)
        return
    path = os.path.join(ROOT, "DESIGN.md")
    text = open(path, encoding="utf-8").read()
    if BEGIN in text and END in text:
        a = text.index(BEGIN)
        b = text.index(END) + len(END)
        text = text[:a] + block + text[b:]
    else:
        text = text.rstrip() + "\n\n" + block + "\n"
    open(path, "w", encoding="utf-8").write(text)
    print("checklist aggiornata: %s" % dict(count))


if __name__ == "__main__":
    main()
