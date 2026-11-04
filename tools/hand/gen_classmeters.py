#!/usr/bin/env python3
"""Phase 7 - class elements as combat cards (DESIGN.md par. 2, 5, 6): medic charge, item effect meters
(all variants), sticky counter, thin charge bars, spy disguise status."""
import glob, os
from _patch import patch, lit, ROOT

def card(name, w="80", t="36"):
    return '''"%s"
{
	"ControlName"			"EditablePanel"
	"fieldName"				"%s"
	"xpos"					"0"
	"ypos"					"0"
	"zpos"					"-1"
	"wide"					"%s"
	"tall"					"%s"
	"visible"				"1"
	"enabled"				"1"
	"paintbackground"		"1"
	"paintbackgroundtype"	"2"
	"bgcolor_override"		"DkCard"
}''' % (name, name, w, t)

HIDE_IMG = {"image": "", "wide": "0", "tall": "0", "visible": "0"}
BAR = {"fgcolor_override": "DkText", "bgcolor_override": "DkChip"}
LABEL = {"font": "TypeLabel", "allcaps": "1", "fgcolor": "DkTextMuted", "textAlignment": "west"}

# --- medic: 88x36 card above the ammo card -----------------------------------------------------
patch("resource/ui/hudmediccharge.res", {
    ("Background",): dict(HIDE_IMG, teambg_2="", teambg_3=""),
    ("ChargeLabel",): dict(LABEL, xpos="8", ypos="5", wide="56", tall="10"),
    ("IndividualChargesLabel",): dict(LABEL, xpos="8", ypos="5", wide="56", tall="10"),
    ("ChargeMeter",): dict(BAR, xpos="8", ypos="22", wide="72", tall="6"),
    ("ChargeMeter1",): dict(BAR, xpos="8", ypos="22", wide="16", tall="6"),
    ("ChargeMeter2",): dict(BAR, xpos="26", ypos="22", wide="16", tall="6"),
    ("ChargeMeter3",): dict(BAR, xpos="44", ypos="22", wide="16", tall="6"),
    ("ChargeMeter4",): dict(BAR, xpos="62", ypos="22", wide="16", tall="6"),
    ("HealthClusterIcon",): HIDE_IMG,
    ("ResistIcon",): {"xpos": "66", "ypos": "2", "wide": "18", "tall": "18"},
}, add=[(None, card("ChargeCard", "88", "36"))], header="""ClaudeHUD: riscritto a mano (fase 7) - carica del Medic: scheda DkCard 88x36 sopra le munizioni,
micro-etichetta + barra squadrata; carica pronta = terracotta fissa (HudMedicCharged).
Generato da tools/hand/gen_classmeters.py""")

# --- item effect meters: one 80x36 card, left of the ammo card --------------------------------
for p in sorted(glob.glob(os.path.join(ROOT, "#TF2 Files", "resource", "ui", "huditemeffectmeter*.res"))):
    rel = "resource/ui/" + os.path.basename(p)
    has_base = open(p, encoding="utf-8", errors="replace").read().lstrip().lower().startswith("#base")
    edits = {
        ("HudItemEffectMeter",): {"xpos": "r184", "ypos": "r48", "wide": "80", "tall": "36"},
        ("ItemEffectMeterBG",): dict(HIDE_IMG, teambg_2="", teambg_3=""),
        ("ItemEffectMeterLabel",): dict(LABEL, xpos="8", ypos="5", wide="64", tall="10"),
        ("ItemEffectMeter",): dict(BAR, xpos="8", ypos="22", wide="64", tall="6"),
        ("ItemEffectMeterCount",): {"xpos": "36", "ypos": "2", "wide": "36", "tall": "18", "font": "NumM",
                                    "fgcolor": "DkText", "textAlignment": "east"},
        ("ItemEffectMeterLabel2",): {"xpos": "8", "ypos": "12", "wide": "64", "tall": "10", "font": "TypeCaption",
                                     "fgcolor": "DkTextMuted"},
        ("ItemEffectIcon",): {"xpos": "52", "ypos": "2", "wide": "20", "tall": "20"},
        ("KillComboClassIcon1",): {"xpos": "48", "ypos": "4", "wide": "8", "tall": "8"},
        ("KillComboClassIcon2",): {"xpos": "56", "ypos": "4", "wide": "8", "tall": "8"},
        ("KillComboClassIcon3",): {"xpos": "64", "ypos": "4", "wide": "8", "tall": "8"},
    }
    patch(rel, edits, optional=True, add=None if has_base else [(None, card("MeterCard"))],
          header="""ClaudeHUD: riscritto a mano (fase 7) - metro dell'oggetto: scheda DkCard 80x36 a sinistra delle
munizioni (r184 / r48), micro-etichetta, barra squadrata DkText su DkChip, contatore NumM.
Generato da tools/hand/gen_classmeters.py""")

# --- demoman sticky counter (same slot) -------------------------------------------------------
pipes = {
    ("background",): dict(HIDE_IMG, teambg_2="", teambg_3=""),
    ("ChargeLabel",): dict(LABEL, xpos="8", ypos="5", wide="64", tall="10"),
    ("ChargeMeter",): dict(BAR, xpos="8", ypos="28", wide="64", tall="4"),
}
for panel_name in ("PipesPresentPanel", "NoPipesPresentPanel"):
    pipes[(panel_name,)] = {"xpos": "0", "ypos": "0", "wide": "80", "tall": "36"}
    pipes[(panel_name, "PipeIcon")] = {"xpos": "8", "ypos": "6", "wide": "18", "tall": "18"}
    pipes[(panel_name, "NumPipesLabel")] = {"xpos": "30", "ypos": "0", "wide": "42", "tall": "28", "font": "NumL",
                                            "fgcolor": "DkText" if panel_name == "PipesPresentPanel" else "DkTextMuted",
                                            "textAlignment": "west"}
    pipes[(panel_name, "NumPipesLabelDropshadow")] = {"fgcolor": "Clear", "wide": "0", "tall": "0"}
patch("resource/ui/huddemomanpipes.res", pipes, add=[(None, card("PipesCard"))],
      header="""ClaudeHUD: riscritto a mano (fase 7) - contatore bombe adesive: scheda DkCard 80x36, numero NumL.
Generato da tools/hand/gen_classmeters.py""")

# --- thin charge bars (shield, bow, flame rocket): 88x4 square bar above the ammo card -----------
for f in ("huddemomancharge.res", "hudbowcharge.res"):
    patch("resource/ui/" + f, {("ChargeMeter",): dict(BAR, xpos="0", ypos="0", wide="88", tall="4")},
          header="""ClaudeHUD: riscritto a mano (fase 7) - barra di carica squadrata 88x4 sopra la scheda munizioni.
Generato da tools/hand/gen_classmeters.py""")

# --- spy disguise status ------------------------------------------------------------------------
patch("resource/ui/disguisestatuspanel.res", {
    ("DisguiseStatusBG",): dict(HIDE_IMG, teambg_1="", teambg_2="", teambg_3=""),
    ("DisguiseNameLabel",): {"xpos": "36", "ypos": "4", "wide": "100", "tall": "12", "font": "TypeBodyStrong",
                             "fgcolor_override": "DkText", "textAlignment": "west"},
    ("WeaponNameLabel",): {"xpos": "36", "ypos": "16", "wide": "100", "tall": "10", "font": "TypeCaption",
                           "fgcolor_override": "DkTextMuted", "textAlignment": "west"},
    ("SpectatorGUIHealth",): {"xpos": "6", "ypos": "4", "wide": "22", "tall": "22"},
    ("itemmodelpanel",): {"xpos": "136", "ypos": "0", "wide": "40", "tall": "30"},
}, add=[(None, card("DisguiseCard", "176", "30"))], header="""ClaudeHUD: riscritto a mano (fase 7) - stato del travestimento della Spy: scheda DkCard 200x30
con chip salute, nome del travestimento e arma. Generato da tools/hand/gen_classmeters.py""")
print("ok")

# --- engineer building status (top-left list): the textured team background is tinted to Clear
#     (the code swaps its icon, not its tint) and a DkCard sits behind it --------------------------
for f in ("hud_obj_dispenser.res", "hud_obj_sapper.res", "hud_obj_sentrygun.res", "hud_obj_sentrygun_disp.res",
          "hud_obj_tele.res", "hud_obj_tele_entrance.res", "hud_obj_tele_exit.res"):
    patch("resource/ui/" + f, {("Background",): {"iconColor": "Clear"},
                                ("BuiltPanel", "AlertTray"): {}},  # Valve duplicate ypos, deduplicated
          optional=True,
          add=[(None, card("BuildingCard", "116", "56").replace('"ypos"\t\t\t\t\t"0"', '"ypos"\t\t\t\t\t"2"').replace('"zpos"\t\t\t\t\t"-1"', '"zpos"\t\t\t\t\t"-2"'))],
          header="""ClaudeHUD: riscritto a mano (fase 7) - stato edificio dell'Engineer: scheda DkCard 116x56,
sfondo testurizzato di squadra reso trasparente (iconColor Clear), barra salute dai token BaseSettings.
Generato da tools/hand/gen_classmeters.py""")
print("ok buildings")
