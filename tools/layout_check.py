#!/usr/bin/env python3
"""
Resolution check (DESIGN.md par. 5): resolves the positions of the main HUD elements at 4:3, 16:10,
16:9 and 21:9 (proportional 480-line space) and reports elements that leave the screen, overlap
each other, or enter the central combat rectangle (c-120..c+120 x c-80..c+80).

Positions supported: N, cN / c-N, rN, f0, fN (the forms used by the ClaudeHUD hand-written files).
  python3 tools/layout_check.py          report
  python3 tools/layout_check.py --json   rectangles for tools/preview.py
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import vdf  # noqa: E402

ASPECTS = {"4:3": 4 / 3, "16:10": 16 / 10, "16:9": 16 / 9, "21:9": 64 / 27}
H = 480.0


def num(expr, full, size=0.0):
    e = str(expr).strip()
    m = re.fullmatch(r"c(-?[\d.]+)", e)
    if m:
        return full / 2 + float(m.group(1))
    m = re.fullmatch(r"r(-?[\d.]+)", e)
    if m:
        return full - float(m.group(1))
    m = re.fullmatch(r"f(-?[\d.]+)", e)
    if m:
        return full - float(m.group(1))
    return float(e)


def load(rel):
    return vdf.parse(open(os.path.join(ROOT, rel), encoding="utf-8", errors="replace").read())


def block(nodes, *path):
    cur = next(nd[1] for nd in nodes if isinstance(nd[1], list))
    for name in path:
        cur = next(nd[1] for nd in cur if isinstance(nd[1], list) and nd[0].lower() == name.lower())
    return {k.lower(): v for k, v, c, cm in cur if not isinstance(v, list) and not (c and "X360" in c)}


def rect(kv, W, Hh=H, ox=0.0, oy=0.0, pw=None, ph=None):
    pw = W if pw is None else pw
    ph = Hh if ph is None else ph
    w = num(kv.get("wide", "0"), pw)
    t = num(kv.get("tall", "0"), ph)
    x = ox + num(kv.get("xpos", "0"), pw)
    y = oy + num(kv.get("ypos", "0"), ph)
    return [round(x, 1), round(y, 1), round(w, 1), round(t, 1)]


def elements(W):
    """name -> [x, y, w, h] in proportional units for screen width W (height 480)."""
    out = {}
    hl = load("scripts/hudlayout.res")
    hp = load("resource/ui/hudplayerhealth.res")
    root = block(hp, "HudPlayerHealth")
    r = rect(root, W)
    card = block(hp, "HealthCard")
    out["Salute (scheda)"] = rect(card, W, ox=r[0], oy=r[1], pw=r[2], ph=r[3])
    out["Salute (icone di stato)"] = [r[0], r[1], r[2], 20]
    pc = load("resource/ui/hudplayerclass.res")
    out["Travestimento Spy (chip)"] = rect(block(pc, "PlayerStatusSpyImage"), W)
    out["Arma trasportata"] = rect(block(pc, "CarryingWeapon"), W)
    for name, label in (("HudWeaponAmmo", "Munizioni"), ("HudMedicCharge", "Carica Medic"),
                        ("HudItemEffectMeter", "Metro oggetto"), ("HudDemomanCharge", "Barra carica"),
                        ("HudChat", "Chat"), ("DisguiseStatus", "Stato travestimento"),
                        ("HudKothTimeStatus", "Timer KOTH")):
        out[label] = rect(block(hl, name), W)
    dn = block(hl, "HudDeathNotice")
    # effective drawn area: notices are right-justified, MaxDeathNotices lines from the top
    lines = int(dn.get("maxdeathnotices", "5"))
    lh = float(dn.get("lineheight", "16")) + float(dn.get("linespacing", "4"))
    out["Killfeed (area)"] = [round(W - 12 - 300, 1), float(dn.get("ypos", "12")), 300.0, lines * lh]
    ms = load("resource/ui/hudmatchstatus.res")
    out["Timer di round"] = rect(block(ms, "ObjectiveStatusTimePanel"), W)
    tid = block(hl, "CMainTargetID")
    out["Target ID"] = [round(W / 2 - 126, 1), float(tid.get("ypos", "0")), 252.0, float(tid.get("tall", "30"))]
    fp = load("resource/ui/hudobjectiveflagpanel.res")
    out["CTF (scheda punteggio)"] = rect(block(fp, "FlagScoreCard"), W)
    es = load("resource/ui/objectivestatusescort.res")
    ek = block(es, "ObjectiveStatusEscort")
    eb = rect(ek, W)
    lb = block(es, "LevelBar")
    out["Carrello (binario)"] = [eb[0] + float(lb["xpos"]), eb[1] + float(lb["ypos"]), float(lb["wide"]), float(lb["tall"])]
    return out


def overlap(a, b):
    return a[0] < b[0] + b[2] and b[0] < a[0] + a[2] and a[1] < b[1] + b[3] and b[1] < a[1] + a[3]


# pairs that are allowed to overlap (mutually exclusive or deliberately stacked)
ALLOWED = {
    frozenset(("Carica Medic", "Barra carica")),          # medic vs demo: never the same class
    frozenset(("Metro oggetto", "Barra carica")),
    frozenset(("Killfeed (area)", "Timer KOTH")),          # killfeed area is the full right column box; entries are right-aligned
    frozenset(("Killfeed (area)", "Timer di round")),
    frozenset(("Killfeed (area)", "Target ID")),
    frozenset(("Killfeed (area)", "Carica Medic")),
    frozenset(("Killfeed (area)", "Munizioni")),
    frozenset(("Killfeed (area)", "Metro oggetto")),
    frozenset(("Killfeed (area)", "Barra carica")),
    frozenset(("Killfeed (area)", "CTF (scheda punteggio)")),
    frozenset(("Killfeed (area)", "Carrello (binario)")),
    frozenset(("Killfeed (area)", "Chat")),
    frozenset(("Killfeed (area)", "Stato travestimento")),
    frozenset(("Timer KOTH", "Timer di round")),            # KOTH replaces the round timer
    frozenset(("CTF (scheda punteggio)", "Carrello (binario)")),  # different game modes
    frozenset(("Salute (icone di stato)", "Salute (scheda)")),
}


def main():
    problems = 0
    report = {}
    for label, aspect in ASPECTS.items():
        W = H * aspect
        els = elements(W)
        report[label] = {"W": W, "elements": els}
        print("== %s (larghezza %d unita')" % (label, W))
        for name, (x, y, w, h) in els.items():
            if x < 0 or y < 0 or x + w > W + 0.5 or y + h > H + 0.5:
                print("   FUORI SCHERMO  %-26s %s" % (name, [x, y, w, h]))
                problems += 1
        names = list(els)
        for i, a in enumerate(names):
            for b in names[i + 1:]:
                if frozenset((a, b)) in ALLOWED:
                    continue
                if overlap(els[a], els[b]):
                    print("   SOVRAPPOSTI    %-26s <-> %s" % (a, b))
                    problems += 1
        centre = [W / 2 - 120, H / 2 - 80, 240, 160]
        for name, r in els.items():
            if name in ("Target ID", "Chat"):  # transient: target ID sits below the crosshair, chat fades out
                continue
            if overlap(r, centre):
                print("   AREA CENTRALE  %s" % name)
                problems += 1
    if "--json" in sys.argv:
        print(json.dumps(report))
    print("\n%d problema/i" % problems)
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
