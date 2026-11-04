#!/usr/bin/env python3
"""Phase 4 objective panels: CTF flag card, flag status, payload track, team goal, alerts."""
from _patch import patch, lit, T

HIDE_IMG = {"image": "", "wide": "0", "tall": "0", "visible": "0"}

def card(name, x, y, w, t, role="DkCard"):
    return '''"%s"
{
	"ControlName"			"EditablePanel"
	"fieldName"				"%s"
	"xpos"					"%s"
	"ypos"					"%s"
	"zpos"					"-1"
	"wide"					"%s"
	"tall"					"%s"
	"visible"				"1"
	"enabled"				"1"
	"paintbackground"		"1"
	"paintbackgroundtype"	"2"
	"bgcolor_override"		"%s"
}''' % (name, name, x, y, w, t, role)

# --- CTF: score card on the bottom rail (centre), flags inside it --------------------------------
patch("resource/ui/hudobjectiveflagpanel.res", {
    ("LeftSideBG",): HIDE_IMG, ("RightSideBG",): HIDE_IMG, ("OutlineBG",): HIDE_IMG,
    ("BlueScore",): {"xpos": "c-108", "ypos": "r56", "wide": "36", "tall": "44", "font": "NumL",
                     "fgcolor": "DkBluText", "textAlignment": "center"},
    ("BlueScoreShadow",): {"fgcolor": "Clear", "wide": "0", "tall": "0"},
    ("RedScore",): {"xpos": "c72", "ypos": "r56", "wide": "36", "tall": "44", "font": "NumL",
                    "fgcolor": "DkRedText", "textAlignment": "center"},
    ("RedScoreShadow",): {"fgcolor": "Clear", "wide": "0", "tall": "0"},
    ("BlueFlag",): {"xpos": "c-135", "ypos": "r77"},
    ("RedFlag",): {"xpos": "c-25", "ypos": "r77"},
    ("PlayingTo",): {"xpos": "c-70", "ypos": "r72", "wide": "140", "tall": "12", "font": "TypeLabel",
                     "fgcolor": "DkTextMuted", "allcaps": "1"},
    ("PlayingToBG",): HIDE_IMG,
}, add=[(None, card("FlagScoreCard", "c-112", "r56", "224", "44"))],
header="""ClaudeHUD: riscritto a mano (fase 4) - CTF: una scheda DkCard 224x44 sul binario inferiore,
punteggio BLU (SteelLight) e RED (Terracotta) in NumL, valigette di gioco al centro.
Generato da tools/hand/gen_objectives.py""")

patch("resource/ui/flagstatus.res", {
    ("Arrow",): {"xpos": "60", "ypos": "23", "wide": "40", "tall": "40"},
}, header="""ClaudeHUD: riscritto a mano (fase 4) - stato della bandiera: freccia ridotta e centrata sulla
valigetta, per stare dentro la scheda CTF. Generato da tools/hand/gen_objectives.py""")

# --- payload: flat track ----------------------------------------------------------------------
patch("resource/ui/objectivestatusescort.res", {
    ("LevelBar",): {"image": "", "fillcolor": lit("DkChip")},
    ("EscortItemPanel", "RecedeTime"): {"font": "NumXS", "fgcolor": "DkText"},
    ("EscortItemPanel", "CapNumPlayers"): {"font": "NumXS", "fgcolor": "DkText"},
}, header="""ClaudeHUD: riscritto a mano (fase 4) - carrello: binario piatto DkChip (niente texture
cart_track), numeri NumXS. Icone del carrello e dei punti restano quelle di gioco (semantica).
Generato da tools/hand/gen_objectives.py""")

# --- team goal / alert: notification cards ----------------------------------------------------
patch("resource/ui/hudteamgoal.res", {
    ("HudTeamGoalBG",): {"image": "", "wide": "0", "tall": "0", "visible": "0", "teambg_2": "", "teambg_3": ""},
    ("GoalImage",): {"xpos": "16", "ypos": "16", "wide": "48", "tall": "48"},
    ("SwitchLabel",): {"xpos": "76", "ypos": "16", "wide": "228", "tall": "14", "font": "TypeBodyStrong",
                       "textAlignment": "west", "fgcolor_override": "DkText"},
    ("GoalLabel",): {"xpos": "76", "ypos": "32", "wide": "228", "tall": "40", "font": "TypeBody",
                     "textAlignment": "north-west", "fgcolor_override": "DkTextMuted"},
}, add=[(None, card("GoalCard", "0", "0", "320", "80"))],
header="""ClaudeHUD: riscritto a mano (fase 4) - obiettivo della squadra: scheda DkCard 320x80,
icona di gioco a sinistra, testo Plex a destra. Generato da tools/hand/gen_objectives.py""")

patch("resource/ui/hudalert.res", {
    ("HudAlertBG",): {"image": "", "wide": "0", "tall": "0", "visible": "0", "teambg_2": "", "teambg_3": ""},
    ("AlertImage",): {"xpos": "16", "ypos": "46", "wide": "48", "tall": "48"},
    ("AlertLabel",): {"xpos": "76", "ypos": "46", "wide": "228", "tall": "48", "font": "TypeBodyStrong",
                      "textAlignment": "north-west", "fgcolor_override": "DkText"},
}, add=[(None, card("AlertCard", "0", "30", "320", "80"))],
header="""ClaudeHUD: riscritto a mano (fase 4) - avviso (bilanciamento squadre ecc.): scheda DkCard.
Generato da tools/hand/gen_objectives.py""")
print("ok")
