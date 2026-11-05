#!/usr/bin/env python3
"""Death and end-of-round screens (dark, in-game): spectator bar with the respawn timer, freeze-cam killer
card, killer health chip, win panel. Element names checked against the TF2 client source
(tf_spectatorgui.cpp, tf_hud_freezepanel.cpp, tf_hud_winpanel.cpp)."""
from _patch import patch, lit

HIDE = {"wide": "0", "tall": "0", "visible": "0"}
HIDE_IMG = dict(HIDE, image="")


def card(name, x, y, w, t, role="DkCard", z="-1"):
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


# ------------------------------------------------------------------ spectator / dead
KEY = {"font": "TypeCaption", "fgcolor": "DkText"}
HINT = {"font": "TypeCaption", "fgcolor": "DkTextMuted"}
patch("resource/ui/spectator.res", {
    ("topbar",): {"bgcolor_override": "Clear"},
    ("bottombarblank",): {"bgcolor_override": "DkCardSoft", "paintbackground": "1"},
    ("ReinforcementsLabel",): {"xpos": "c-140", "ypos": "56", "wide": "280", "tall": "22", "font": "TypeBodyStrong",
                               "fgcolor": "DkText", "textAlignment": "center", "paintbackground": "1",
                               "paintbackgroundtype": "2", "bgcolor_override": "DkCard"},
    ("BuyBackLabel",): {"font": "TypeBody", "fgcolor": "DkAccent"},
    ("MapLabel",): {"font": "TypeCaption", "fgcolor": "DkTextMuted"},
    ("ClassOrTeamLabel",): HINT,
    ("SwitchCamModeKeyLabel",): KEY, ("SwitchCamModeLabel",): HINT,
    ("CycleTargetFwdKeyLabel",): KEY, ("CycleTargetFwdLabel",): HINT,
    ("CycleTargetRevKeyLabel",): KEY, ("CycleTargetRevLabel",): HINT,
    ("TipLabel",): HINT,
    ("itempanel",): {"bgcolor_override": "DkCard"},
}, optional=True, header="""ClaudeHUD: riscritto a mano - spettatore / attesa del respawn: fascia inferiore DkCardSoft con i tasti,
tempo di rinascita in una chip DkCard centrata in alto, mappa e suggerimenti attenuati.
Generato da tools/hand/gen_deathscreens.py""")


# ------------------------------------------------------------------ freeze-cam killer card
def drop_first_base(root):
    """freezepanel_basic.res defines FreezePanelBase twice; the game applies both, the second wins.
    Keep only the effective (second) block."""
    idx = [i for i, nd in enumerate(root) if isinstance(nd[1], list) and nd[0].lower() == "freezepanelbase"]
    if len(idx) > 1:
        del root[idx[0]]


patch("resource/ui/freezepanel_basic.res", {
    ("FreezePanelBase", "FreezePanelBG"): dict(HIDE_IMG, teambg_1="", teambg_2="", teambg_3=""),
    ("FreezePanelBase", "FreezeLabel"): {"xpos": "46", "ypos": "161", "wide": "200", "tall": "10", "font": "TypeLabel",
                                         "allcaps": "1", "fgcolor_override": "DkTextMuted"},
    ("FreezePanelBase", "FreezeLabelKiller"): {"xpos": "61", "ypos": "171", "wide": "190", "tall": "16",
                                               "font": "TypeBodyStrong", "fgcolor_override": "DkText"},
    ("FreezePanelBase", "FreezePanelHealth"): {"xpos": "12", "ypos": "161", "wide": "30", "tall": "30"},
    ("FreezePanelBase", "AvatarImage"): {"xpos": "46", "ypos": "173", "wide": "14", "tall": "14"},
    ("itempanel",): {"bgcolor_override": "DkCard"},
    ("ScreenshotPanel", "ScreenshotPanelBG"): {"image": "", "fillcolor": "DkCard"},
    ("ScreenshotPanel", "ScreenshotLabel"): {"font": "TypeCaption", "fgcolor_override": "DkText"},
}, pre=drop_first_base, add=[(("FreezePanelBase",), card("KillerCard", "8", "158", "256", "36"))],
   header="""ClaudeHUD: riscritto a mano - killcam: scheda DkCard 256x36 con chip della salute dell'avversario,
"Ucciso da" in micro-etichetta e nome in Plex. Il file Valve definisce FreezePanelBase due volte:
resta solo il blocco effettivo (il secondo). Generato da tools/hand/gen_deathscreens.py""")

patch("resource/ui/freezepanelkillerhealth.res", {
    ("PlayerStatusHealthImage",): dict(HIDE, enabled="0"),
    ("PlayerStatusHealthImageBG",): HIDE_IMG,
    ("BuildingStatusHealthImageBG",): HIDE_IMG,
    ("PlayerStatusHealthBonusImage",): HIDE_IMG,
    ("PlayerStatusHealthValue",): {"xpos": "0", "ypos": "0", "wide": "30", "tall": "30", "font": "NumS",
                                   "fgcolor": "DkText", "textAlignment": "center"},
}, add=[(None, card("HealthChip", "0", "0", "30", "30", "DkChip", z="1"))],
   header="""ClaudeHUD: riscritto a mano - salute dell'avversario nella killcam: chip DkChip 30x30 con il numero.
Generato da tools/hand/gen_deathscreens.py""")

# ------------------------------------------------------------------ win panel
TS = ("TeamScoresPanel",)
E = {
    ("WinPanelBGBorder",): {"bgcolor_override": "DkCard"},  # neutral: the winner's colour is on the scores
    TS + ("BlueScoreBG",): {"bgcolor_override": "DkBluFill"},
    TS + ("RedScoreBG",): {"bgcolor_override": "DkRedFill"},
    TS + ("BlueTeamLabel",): {"font": "TypeLabel", "allcaps": "1", "fgcolor": "DkOnBlu"},
    TS + ("RedTeamLabel",): {"font": "TypeLabel", "allcaps": "1", "fgcolor": "DkOnRed"},
    TS + ("BlueTeamScore",): {"font": "NumXL", "fgcolor": "DkOnBlu"},
    TS + ("RedTeamScore",): {"font": "NumXL", "fgcolor": "DkOnRed"},
    TS + ("BlueTeamScoreDropshadow",): dict(HIDE, fgcolor="Clear"),
    TS + ("RedTeamScoreDropshadow",): dict(HIDE, fgcolor="Clear"),
    TS + ("BlueLeaderAvatarBG",): {"bgcolor_override": "DkCard"},
    TS + ("RedLeaderAvatarBG",): {"bgcolor_override": "DkCard"},
    ("WinningTeamLabel",): {"font": "NumL", "fgcolor": "DkText"},
    ("WinningTeamLabelDropshadow",): dict(HIDE, fgcolor="Clear"),
    ("AdvancingTeamLabel",): {"font": "TypeBodyStrong", "fgcolor": "DkText"},
    ("AdvancingTeamLabelDropshadow",): dict(HIDE, fgcolor="Clear"),
    ("WinReasonLabel",): {"font": "TypeCaption", "fgcolor": "DkTextMuted"},
    ("DetailsLabel",): {"font": "TypeCaption", "fgcolor": "DkTextMuted"},
    ("ShadedBar",): HIDE,
    ("TopPlayersLabel",): {"font": "TypeLabel", "allcaps": "1", "fgcolor": "DkTextMuted"},
    ("PointsThisRoundLabel",): {"font": "TypeLabel", "allcaps": "1", "fgcolor": "DkTextMuted"},
    ("KillStreakLeaderLabel",): {"font": "TypeLabel", "allcaps": "1", "fgcolor": "DkTextMuted"},
    ("KillStreakMaxCountLabel",): {"font": "TypeLabel", "allcaps": "1", "fgcolor": "DkTextMuted"},
    ("HorizontalLine",): {"fillcolor": "DkLine"},
    ("HorizontalLine2",): {"fillcolor": "DkLine"},
}
for pre in ("Player1", "Player2", "Player3", "KillStreakPlayer1"):
    E[(pre + "Name",)] = {"font": "TypeBody", "fgcolor": "DkText"}
    E[(pre + "Class",)] = {"font": "TypeCaption", "fgcolor": "DkTextMuted"}
    E[(pre + "Score",)] = {"font": "NumS", "fgcolor": "DkText"}
patch("resource/ui/winpanel.res", E, optional=True, header="""ClaudeHUD: riscritto a mano - fine round: scheda neutra DkCard (il vincitore e' nei riquadri punteggio
pieni Steel / Terracotta), titolo in Plex SemiBold, classifica con nomi Plex e punteggi NumS,
filetti DkLine. Generato da tools/hand/gen_deathscreens.py""")
print("ok death screens")
