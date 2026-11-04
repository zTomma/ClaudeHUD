#!/usr/bin/env python3
"""Replace selected events in scripts/hudanimations_tf.txt with the ClaudeHUD motion rule (DESIGN.md par. 7).
Rule: in 0.20 Deaccel, out 0.15 Accel, colour state 0.12 Linear, danger = 2 Hz loop (0.5 s)."""
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(os.path.dirname(HERE))
PATH = os.path.join(ROOT, "scripts", "hudanimations_tf.txt")

EVENTS = {}
def ev(name, body):
    EVENTS[name] = "event %s\n{\n%s\n}" % (name, "\n".join("\t" + l for l in body.strip().split("\n")))

# --- health -------------------------------------------------------------------------------
ev("HudHealthBonusPulse", '''
// overheal: il numero passa a Sage (stato positivo), nessuna pulsazione
Animate	PlayerStatusHealthValue	FgColor	"DkPositive"	Linear 0.0 0.12
RunEvent HudHealthBonusPulseLoop	0.5''')
ev("HudHealthBonusPulseLoop", '''RunEvent HudHealthBonusPulse 0.0''')
ev("HudHealthBonusPulseStop", '''
StopEvent HudHealthBonusPulse 0.0
StopEvent HudHealthBonusPulseLoop 0.0
Animate	PlayerStatusHealthValue	FgColor	"DkText"	Linear 0.0 0.12''')
ev("HudHealthDyingPulse", '''
// pericolo: numero terracotta fisso + il Segno pulsa a 2 Hz
Animate	PlayerStatusHealthValue	FgColor	"DkAccent"	Linear 0.0 0.12
Animate	HealthSegno		Alpha	"255"	Linear 0.0 0.12
Animate	HealthSegno		Alpha	"72"	Linear 0.25 0.12
RunEvent HudHealthDyingPulseLoop	0.5''')
ev("HudHealthDyingPulseLoop", '''RunEvent HudHealthDyingPulse 0.0''')
ev("HudHealthDyingPulseStop", '''
StopEvent HudHealthDyingPulse 0.0
StopEvent HudHealthDyingPulseLoop 0.0
Animate	PlayerStatusHealthValue	FgColor	"DkText"	Linear 0.0 0.12
Animate	HealthSegno		Alpha	"0"	Accel 0.0 0.15''')
# --- ammo ---------------------------------------------------------------------------------
ev("HudLowAmmoPulse", '''
// munizioni basse: numero terracotta + il Segno della scheda munizioni pulsa a 2 Hz
Animate	AmmoInClip		FgColor	"DkAccent"	Linear 0.0 0.12
Animate	AmmoNoClip		FgColor	"DkAccent"	Linear 0.0 0.12
Animate	HudWeaponLowAmmoImage	Alpha	"255"	Linear 0.0 0.12
Animate	HudWeaponLowAmmoImage	Alpha	"72"	Linear 0.25 0.12
RunEvent HudLowAmmoPulseLoop	0.5''')
ev("HudLowAmmoPulseLoop", '''RunEvent HudLowAmmoPulse 0.0''')
ev("HudLowAmmoPulseStop", '''
StopEvent HudLowAmmoPulse 0.0
StopEvent HudLowAmmoPulseLoop 0.0
Animate	AmmoInClip		FgColor	"DkText"	Linear 0.0 0.12
Animate	AmmoNoClip		FgColor	"DkText"	Linear 0.0 0.12
Animate	HudWeaponLowAmmoImage	Alpha	"0"	Accel 0.0 0.15''')

def main():
    text = open(PATH, encoding="utf-8").read()
    for name, block in EVENTS.items():
        pat = re.compile(r"^event\s+%s\s*\n\{.*?^\}" % re.escape(name), re.S | re.M)
        if not pat.search(text):
            raise SystemExit("event not found: " + name)
        text = pat.sub(lambda m: block, text, count=1)
    if "ClaudeHUD: riscritto" not in text[:300]:
        text = text.replace("// ClaudeHUD: animazioni - colori migrati ai token (DESIGN.md par. 7)",
                            "// ClaudeHUD: riscritto a mano (eventi salute/munizioni/obiettivi/classe) + colori migrati ai token.\n"
                            "// Regola unica, DESIGN.md par. 7: entrata 0.20 Deaccel, uscita 0.15 Accel, stato 0.12 Linear,\n"
                            "// pericolo = ciclo a 2 Hz. Eventi aggiornati da tools/hand/patch_anims.py", 1)
    open(PATH, "w", encoding="utf-8", newline="\n").write(text)
    print("patched", len(EVENTS), "events")

if __name__ == "__main__":
    main()
