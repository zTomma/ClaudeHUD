#!/usr/bin/env python3
"""resource/ui/scoreboard.res - light editorial page with dark data tables (DESIGN.md par. 9 exception:
rows coloured by the game's code by team stay on dark surfaces, where the contrast is verified)."""
from _patch import patch, lit

HIDE = {"wide": "0", "tall": "0", "visible": "0"}
HIDE_IMG = dict(HIDE, image="")

def panel(name, x, y, w, t, role, z="-1"):
    return '''"%s"
{
	"ControlName"			"EditablePanel"
	"fieldName"				"%s"
	"xpos"					"%s"
	"ypos"					"%s"
	"zpos"					"%s"
	"wide"					"%s"
	"tall"					"%s"
	"visible"				"1"
	"enabled"				"1"
	"paintbackground"		"1"
	"paintbackgroundtype"	"2"
	"bgcolor_override"		"%s"
}''' % (name, name, x, y, z, w, t, role)

E = {
    # header: two team bands, team name (serif) + player count on the left, score (serif display) on the right
    ("BlueScoreBG",): HIDE_IMG, ("RedScoreBG",): HIDE_IMG,
    ("BlueTeamImage",): HIDE_IMG, ("RedTeamImage",): HIDE_IMG,
    ("BlueLeaderAvatar",): {"xpos": "222", "ypos": "4", "wide": "28", "tall": "28", "zpos": "5"},
    ("BlueLeaderAvatarBG",): {"xpos": "221", "ypos": "3", "wide": "30", "tall": "30", "zpos": "4", "bgcolor_override": "LtCard"},
    ("RedLeaderAvatar",): {"xpos": "390", "ypos": "4", "wide": "28", "tall": "28", "zpos": "5"},
    ("RedLeaderAvatarBG",): {"xpos": "389", "ypos": "3", "wide": "30", "tall": "30", "zpos": "4", "bgcolor_override": "LtCard"},
    ("BlueTeamLabel",): {"xpos": "12", "ypos": "2", "wide": "200", "tall": "20", "zpos": "20", "visible": "1",
                         "font": "TypeHeading", "fgcolor": "LtOnBlu", "textAlignment": "west"},
    ("BlueTeamPlayerCount",): {"xpos": "12", "ypos": "21", "wide": "200", "tall": "12", "zpos": "20",
                               "font": "TypeCaption", "fgcolor": "LtOnBlu", "textAlignment": "west"},
    ("BlueTeamScore",): {"xpos": "252", "ypos": "0", "wide": "56", "tall": "36", "zpos": "20",
                         "font": "TypeTitle", "fgcolor": "LtOnBlu", "textAlignment": "east"},
    ("BlueTeamScoreDropshadow",): dict(HIDE, fgcolor="Clear"),
    ("RedTeamLabel",): {"xpos": "428", "ypos": "2", "wide": "200", "tall": "20", "zpos": "20", "visible": "1",
                        "font": "TypeHeading", "fgcolor": "LtOnRed", "textAlignment": "east"},
    ("RedTeamPlayerCount",): {"xpos": "428", "ypos": "21", "wide": "200", "tall": "12", "zpos": "20",
                              "font": "TypeCaption", "fgcolor": "LtOnRed", "textAlignment": "east"},
    ("RedTeamScore",): {"xpos": "332", "ypos": "0", "wide": "56", "tall": "36", "zpos": "20",
                        "font": "TypeTitle", "fgcolor": "LtOnRed", "textAlignment": "west"},
    ("RedTeamScoreDropshadow",): dict(HIDE, fgcolor="Clear"),
    # page and tables
    ("MainBG",): {"xpos": "0", "ypos": "40", "wide": "640", "tall": "408", "zpos": "-2", "bgcolor_override": "LtCanvas"},
    ("BluePlayerList",): {"xpos": "4", "ypos": "48", "wide": "308", "tall": "288", "zpos": "20", "bgcolor_override": "Clear"},
    ("RedPlayerList",): {"xpos": "328", "ypos": "48", "wide": "308", "tall": "288", "zpos": "20", "bgcolor_override": "Clear"},
    ("VerticalLine",): HIDE,
    ("Spectators",): {"xpos": "12", "ypos": "346", "wide": "616", "tall": "10", "font": "TypeCaption",
                      "fgcolor": "LtTextMuted", "textAlignment": "west"},
    ("SpectatorsInQueue",): {"xpos": "12", "ypos": "356", "wide": "616", "tall": "10", "font": "TypeCaption",
                             "fgcolor": "LtTextMuted", "textAlignment": "west"},
    # timer: moved into the bottom card (right column)
    ("TimerBG",): HIDE, ("ServerTimeLeftInsetBG",): HIDE,
    ("ServerTimeLeftLabel",): {"xpos": "496", "ypos": "398", "wide": "128", "tall": "10", "font": "TypeLabel",
                               "allcaps": "1", "fgcolor": "LtTextMuted", "textAlignment": "east"},
    ("ServerTimeLeftValue",): {"xpos": "496", "ypos": "408", "wide": "128", "tall": "24", "font": "TypeSerifNum",
                               "fgcolor": "LtText", "textAlignment": "east"},
    ("ServerTimeLeft",): HIDE, ("ServerLabel",): HIDE,
    # bottom card: local player
    ("ShadedBar",): HIDE,
    ("ClassImage",): HIDE_IMG,
    ("classmodelpanel",): {"wide": "0", "tall": "0", "visible": "0"},
    ("PlayerNameBG",): {"xpos": "0", "ypos": "368", "wide": "640", "tall": "80", "zpos": "-1", "bgcolor_override": "LtCard"},
    ("PlayerNameLabel",): {"xpos": "16", "ypos": "372", "wide": "300", "tall": "22", "font": "TypeHeading",
                           "fgcolor": "LtText", "textAlignment": "west"},
    ("ServerLabelNew",): {"xpos": "324", "ypos": "374", "wide": "300", "tall": "11", "font": "TypeCaption",
                          "fgcolor": "LtTextMuted", "textAlignment": "east"},
    ("MapName",): {"xpos": "324", "ypos": "385", "wide": "300", "tall": "11", "font": "TypeBodyStrong",
                   "fgcolor": "LtText", "textAlignment": "east"},
    ("HorizontalLine",): {"xpos": "16", "ypos": "396", "wide": "608", "tall": "1", "visible": "1", "fillcolor": lit("LtLine")},
    ("PlayerScoreLabel",): {"font": "TypeSerifNum", "fgcolor": "LtText"},
    ("LocalPlayerStatsPanel",): {"xpos": "-60", "ypos": "400", "wide": "560", "tall": "48"},
    ("LocalPlayerDuelStatsPanel",): {"ypos": "398"},
    ("LocalPlayerStatsPanel", "BonusLabel"): {},  # Valve duplicate zpos, deduplicated
}
patch("resource/ui/scoreboard.res", E,
      add=[(None, panel("BlueBand", "0", "0", "316", "36", "LtBluFill")),
           (None, panel("RedBand", "324", "0", "316", "36", "LtRedFill")),
           (None, panel("BlueTable", "0", "44", "316", "296", "DkCard")),
           (None, panel("RedTable", "324", "44", "316", "296", "DkCard"))],
      header="""ClaudeHUD: riscritto a mano (fase 5) - scoreboard, variante chiara editoriale.
Pagina avorio, fasce di squadra piene (Steel / Terracotta) con nome serif e punteggio Source Serif
Display; le due tabelle giocatori sono schede DkCard perche' il gioco colora le righe per squadra
dal codice (eccezione di leggibilita', DESIGN.md par. 9). Scheda inferiore bianca con il giocatore
locale, mappa, server e tempo rimasto (numero serif). Generato da tools/hand/gen_scoreboard.py""")
print("ok")
