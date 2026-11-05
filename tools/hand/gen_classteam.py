#!/usr/bin/env python3
"""Light editorial class and team menus (DESIGN.md par. 9): ivory canvas over the game, serif title,
flat buttons (primary = Ink, hover = Terracotta), team cards in the team fills."""
from _patch import patch, lit

HIDE = {"wide": "0", "tall": "0", "visible": "0"}
CANVAS = {"infocus_bgcolor_override": lit("LtCanvasVeil"), "outoffocus_bgcolor_override": lit("LtCanvasVeil")}

def btn(x, y, primary=False, w="148", t="28"):
    d = {"xpos": x, "ypos": y, "wide": w, "tall": t, "font": "TypeBodyStrong", "paintbackground": "1",
         "paintbackgroundtype": "2", "textAlignment": "center",
         "defaultBgColor_override": "LtButton" if primary else "LtCardAlt",
         "defaultFgColor_override": "LtOnButton" if primary else "LtText",
         "armedBgColor_override": "LtButtonHover", "armedFgColor_override": "LtOnButtonHover",
         "depressedBgColor_override": "LtButtonHover", "depressedFgColor_override": "LtOnButtonHover"}
    return d

def label(name, text, x, y, w, t, font, color, align="west"):
    return '''"%s"
{
	"ControlName"			"CExLabel"
	"fieldName"				"%s"
	"xpos"					"%s"
	"ypos"					"%s"
	"zpos"					"7"
	"wide"					"%s"
	"tall"					"%s"
	"visible"				"1"
	"enabled"				"1"
	"mouseinputenabled"		"0"
	"labelText"				"%s"
	"textAlignment"			"%s"
	"font"					"%s"
	"fgcolor"				"%s"
}''' % (name, name, x, y, w, t, text, align, font, color)

# ------------------------------------------------------------------- class selection
E = {
    ("class",): CANVAS,
    ("MenuBG",): HIDE, ("ShadedBar",): dict(HIDE, image=""), ("localPlayerBG",): dict(HIDE, image=""),
    ("ClassMenuSelect",): {"xpos": "32", "ypos": "r76", "wide": "500", "tall": "32", "font": "TypeTitle", "fgcolor": "LtText"},
    ("CancelButton",): btn("r324", "r44"),
    ("EditLoadoutButton",): btn("r168", "r44", primary=True),
    ("ResetButton",): btn("r480", "r44"),
    ("CountLabel",): {"font": "TypeCaption", "fgcolor": "LtTextMuted"},
    ("Footer",): {"fgcolor": "LtText"},
}
for cat in ("Offense", "Defense", "Support"):
    E[(cat,)] = {"font": "TypeLabel", "allcaps": "1", "fgcolor": "LtTextMuted"}
for n in ("numScout", "numSoldier", "numPyro", "numDemoman", "numHeavy", "numEngineer", "numMedic", "numSniper", "numSpy"):
    E[(n,)] = {"font": "TypeCaption", "fgcolor": "LtTextMuted"}
patch("resource/ui/classselection.res", E, header="""ClaudeHUD: riscritto a mano (fase 5) - selezione classe, variante chiara editoriale.
Tela avorio sopra il gioco (niente stanza 3D), titolo Source Serif Display in basso a sinistra,
categorie in micro-etichette, bottoni piatti arrotondati: primario Ink, hover Terracotta.
I ritratti delle classi e il modello 3D restano (illustrazioni di gioco).
Generato da tools/hand/gen_classteam.py""")

# ------------------------------------------------------------------- team menu
def team_button(x, fill, fg):
    return {"xpos": x, "ypos": "120", "wide": "132", "tall": "180", "zpos": "3", "font": "NumS",
            "textAlignment": "south-west", "textinsetx": "8", "paintbackground": "1", "paintbackgroundtype": "2",
            "defaultBgColor_override": fill, "armedBgColor_override": fill, "depressedBgColor_override": fill,
            "selectedBgColor_override": fill, "defaultFgColor_override": fg, "armedFgColor_override": fg,
            "depressedFgColor_override": fg, "border_default": "ClCard", "border_armed": "ClMarkLt", "fgcolor": fg}
E = {
    ("team",): CANVAS,
    ("MenuBG",): HIDE, ("bluedoor",): HIDE, ("reddoor",): HIDE, ("autodoor",): HIDE, ("spectate",): HIDE,
    ("ShadedBar",): dict(HIDE, image=""), ("MapInfo",): HIDE, ("mapname",): HIDE,
    ("TeamMenuSelect",): {"xpos": "32", "ypos": "r76", "wide": "500", "tall": "32", "font": "TypeTitle", "fgcolor": "LtText"},
    ("teambutton2",): team_button("c-282", "LtCard", "LtTextMuted"),
    ("teambutton0",): team_button("c-138", "LtBluFill", "LtOnBlu"),
    ("teambutton1",): team_button("c6", "LtRedFill", "LtOnRed"),
    ("teambutton3",): team_button("c150", "LtCardAlt", "LtTextMuted"),
    ("TeamMenuAuto",): {"xpos": "c-274", "ypos": "128", "wide": "116", "tall": "24", "zpos": "7", "font": "TypeHeading",
                        "fgcolor": "LtText", "textAlignment": "west", "mouseinputenabled": "0"},
    ("TeamMenuSpectate",): {"xpos": "c158", "ypos": "128", "wide": "116", "tall": "24", "zpos": "7", "font": "TypeHeading",
                            "fgcolor": "LtText", "textAlignment": "west", "mouseinputenabled": "0"},
    ("BlueCount",): {"xpos": "c-130", "ypos": "156", "wide": "116", "tall": "32", "zpos": "7", "font": "TypeTitle",
                     "fgcolor": "LtOnBlu", "textAlignment": "west", "mouseinputenabled": "0"},
    ("RedCount",): {"xpos": "c14", "ypos": "156", "wide": "116", "tall": "32", "zpos": "7", "font": "TypeTitle",
                    "fgcolor": "LtOnRed", "textAlignment": "west", "mouseinputenabled": "0"},
    ("CancelButton",): btn("r168", "r44"),
    ("HighlanderLabel",): {"xpos": "c-282", "ypos": "308", "wide": "300", "tall": "14", "font": "TypeBodyStrong", "fgcolor": "LtAccentText"},
    ("HighlanderLabelShadow",): dict(HIDE, fgcolor="Clear"),
    ("TeamsFullLabel",): {"xpos": "c-282", "ypos": "324", "wide": "300", "tall": "14", "font": "TypeBodyStrong", "fgcolor": "LtAccentText"},
    ("TeamsFullLabelShadow",): dict(HIDE, fgcolor="Clear"),
    ("Footer",): {"fgcolor": "LtText"},
}
patch("resource/ui/teammenu.res", E,
      add=[(None, label("BlueTeamName", "#TF_BlueTeam_Name", "c-130", "128", "116", "24", "TypeHeading", "LtOnBlu")),
           (None, label("RedTeamName", "#TF_RedTeam_Name", "c14", "128", "116", "24", "TypeHeading", "LtOnRed"))],
      header="""ClaudeHUD: riscritto a mano (fase 5) - selezione squadra, variante chiara editoriale.
Quattro schede piatte allineate (Casuale, BLU, RED, Spettatore) al posto delle porte 3D: fasce piene
Steel / Terracotta per le squadre, nome serif, numero giocatori in Source Serif Display; in hover il
Segno (bordo ClMarkLt) invece di cambiare colore, per non confondere le squadre.
Generato da tools/hand/gen_classteam.py""")
print("ok")
