#!/usr/bin/env python3
"""
Rebuild the whole HUD from the tokens and the pristine originals, then verify.
    python3 tools/build.py
Order: token migration -> hand-written generators/patches -> schemes (scan alpha variants)
       -> checks (fonts, contrast, lint) -> coverage checklist in DESIGN.md
"""
import os, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
STEPS = [
    ["migrate.py"],
    ["hand/migrate_anims.py"], ["hand/patch_anims.py"],
    ["hand/gen_health.py"], ["hand/patch_hudlayout.py"],
]
EXTRA = sorted(f for f in os.listdir(os.path.join(HERE, "hand")) if f.startswith("gen_") and f != "gen_health.py")
STEPS += [["hand/" + f] for f in EXTRA]
STEPS += [["build_scheme.py"], ["build_scheme.py", "--aux"], ["check_fonts.py"], ["contrast.py"], ["context_contrast.py"], ["lint.py"],
          ["layout_check.py"], ["coverage.py"], ["preview.py"], ["render_res.py"]]

def main():
    for step in STEPS:
        r = subprocess.run([sys.executable, os.path.join(HERE, step[0])] + step[1:], capture_output=True, text=True)
        tail = (r.stdout.strip().splitlines() or [""])[-1]
        print("%-4s %-28s %s" % ("ok" if r.returncode == 0 else "FAIL", " ".join(step), tail))
        if r.returncode:
            print(r.stdout[-3000:], r.stderr[-3000:])
            sys.exit(1)

if __name__ == "__main__":
    main()
