#!/usr/bin/env python3
"""Main menu (light editorial page) + matchmaking top bar. DESIGN.md par. 1, 2, 4, 9."""
import os
from _patch import patch, lit, ROOT

HIDE = {"wide": "0", "tall": "0", "visible": "0"}

def light_btn(x=None, y=None, w=None, t=None, primary=False, icon=True):
    d = {"font": "TypeBodyStrong", "paintbackground": "1", "paintbackgroundtype": "2",
         "border_default": "ClCard", "border_armed": "ClCard",
         "defaultBgColor_override": "LtButton" if primary else "LtCardAlt",
         "defaultFgColor_override": "LtOnButton" if primary else "LtText",
         "armedBgColor_override": "LtButtonHover", "armedFgColor_override": "LtOnButtonHover",
         "depressedBgColor_override": "LtButtonHover", "depressedFgColor_override": "LtOnButtonHover"}
    if icon:
        d.update({"image_drawcolor": "LtOnButton" if primary else "LtTextMuted", "image_armedcolor": "LtOnButtonHover"})
    for k, v in (("xpos", x), ("ypos", y), ("wide", w), ("tall", t)):
        if v is not None:
            d[k] = v
    return d

ICON_BTN = {"paintbackground": "0", "defaultBgColor_override": "Clear", "armedBgColor_override": "Clear",
            "depressedBgColor_override": "Clear", "image_drawcolor": "LtTextMuted", "image_armedcolor": "LtAccent",
            "defaultFgColor_override": "LtText", "armedFgColor_override": "LtAccentText",
            "depressedFgColor_override": "LtAccentText"}

def label(name, text, x, y, w, t, font, color, z="2", align="west"):
    return '''"%s"
{
	"ControlName"	"CExLabel"
	"fieldName"		"%s"
	"xpos"			"%s"
	"ypos"			"%s"
	"zpos"			"%s"
	"wide"			"%s"
	"tall"			"%s"
	"visible"		"1"
	"enabled"		"1"
	"mouseinputenabled"	"0"
	"labelText"		"%s"
	"textAlignment"	"%s"
	"font"			"%s"
	"fgcolor"		"%s"
}''' % (name, name, x, y, z, w, t, text, align, font, color)

SEGNO = '''"ClaudeTitleSegno"
{
	"ControlName"	"ImagePanel"
	"fieldName"		"ClaudeTitleSegno"
	"xpos"			"c-290"
	"ypos"			"52"
	"zpos"			"2"
	"wide"			"2"
	"tall"			"36"
	"visible"		"1"
	"enabled"		"1"
	"fillcolor"		"%s"	// token: LtAccent
}''' % lit("LtAccent")[0]

CANVAS = '''"ClaudeCanvas"
{
	"ControlName"			"EditablePanel"
	"fieldName"				"ClaudeCanvas"
	"xpos"					"0"
	"ypos"					"0"
	"zpos"					"-210"
	"wide"					"f0"
	"tall"					"480"
	"visible"				"1"
	"enabled"				"1"
	"mouseinputenabled"		"0"
	"paintbackground"		"1"
	"bgcolor_override"		"LtCanvas"
}'''

E = {
    ("MainMenuOverride",): {"paintbackground": "1", "bgcolor_override": "LtCanvas"},
    ("MainMenuOverride", "button_kv", "SubButton"): {
        "font": "TypeBodyL", "textinsetx": "25", "paintbackground": "0", "border_default": "NoBorder",
        "border_armed": "ClMarkLt", "defaultFgColor_override": "LtText", "armedFgColor_override": "LtAccentText",
        "depressedFgColor_override": "LtAccentText", "image_drawcolor": "LtTextMuted", "image_armedcolor": "LtAccent"},
    ("mouseoveritempanel",): {"bgcolor_override": "DkCard"},
    ("TFLogoImage",): dict(HIDE, image=""),
    ("TFCharacterImage",): HIDE,
    ("RankBorder",): {"xpos": "c-282", "ypos": "100", "wide": "256", "tall": "56"},
    ("RankPanel",): {"xpos": "c-342", "ypos": "78"},
    ("RankTooltipPanel",): {"xpos": "c-277", "ypos": "105"},
    ("NoGCMessage",): {"xpos": "c-282", "ypos": "100", "font": "TypeCaption", "fgcolor_override": "LtTextMuted"},
    ("NoGCImage",): {"xpos": "c-277", "ypos": "113"},
    ("TooltipPanel",): {"bgcolor_override": "DkCard"},
    ("TooltipPanel", "TipLabel"): {"font": "TypeBodyStrong", "fgcolor": "DkText", "fgcolor_override": "DkText"},
    ("TooltipPanel", "TipSubLabel"): {"font": "TypeBody", "fgcolor": "DkTextMuted", "fgcolor_override": "DkTextMuted"},
    ("EventPromo",): {"xpos": "c-282", "ypos": "164"},
    ("SafeMode",): {"xpos": "c-282", "ypos": "214"},
    ("FriendsContainer",): {"xpos": "c-282", "ypos": "268", "wide": "256", "tall": "148"},
    ("FriendsContainer", "TitleLabel"): {"font": "TypeHeading", "fgcolor": "LtText", "fgcolor_override": "LtText"},
    ("FriendsContainer", "BelowDarken"): {"bgcolor_override": "Clear"},
    ("VRBGPanel",): {"xpos": "c-282", "ypos": "376"},
    ("VRModeButton",): {"xpos": "c-277", "ypos": "382"},
    ("BackgroundFooter",): dict(HIDE, image=""),
    ("FooterLine",): {"xpos": "0", "ypos": "424", "wide": "f0", "tall": "1", "image": "", "fillcolor": lit("LtLine")},
    ("CharacterSetupButton",): light_btn("c-282", None, "100", "26"),
    ("GeneralStoreButton",): light_btn("c-178", None, "100", "26"),
    ("ShowPromoCodesButton",): light_btn(icon=False),
    ("BackToReplaysButton",): light_btn(),
}
for b in ("SettingsButton", "TF2SettingsButton", "SettingsButtonSDK", "TF2SettingsButtonSDK", "NewUserForumsButton",
          "AchievementsButton", "CommentaryButton", "CoachPlayersButton", "WorkshopButton", "ReplayButton", "ReportBugButton"):
    E[(b,)] = ICON_BTN
for b in ("ReportPlayerButton", "CallVoteButton", "MutePlayersButton", "RequestCoachButton", "WatchStreamButton", "QuestLogButton"):
    E[(b, "SubButton")] = ICON_BTN
E[("MOTD_ShowButtonPanel", "MOTD_ShowButtonPanel_SB")] = ICON_BTN
# Valve's original repeats a few keys in these elements: deduplicated (first value kept)
for path in (("CycleRankTypeButton",), ("SafeMode", "Background", "Explanation"),
             ("TF2SettingsButtonSDK", "SubImage"), ("TF2SettingsButton", "SubImage")):
    E.setdefault(path, {})
E[("Notifications_ShowButtonPanel", "Notifications_ShowButtonPanel_SB")] = ICON_BTN

patch("resource/ui/mainmenuoverride.res", E,
      add=[(None, CANVAS), (None, SEGNO),
           (None, label("ClaudeTitle", "Team Fortress 2", "c-282", "48", "420", "42", "TypeDisplay", "LtText"))],
      header="""ClaudeHUD: riscritto a mano (fase 6) - menu principale, variante chiara editoriale.
Pagina avorio (niente sfondo di mappa ne' illustrazione), titolo tipografico Source Serif Display con
il Segno, colonna sinistra allineata a c-282 (grado, evento, amici), bottoni piatti arrotondati,
icone di servizio monocromatiche (hover terracotta). Tooltip scuri. Nessun logo.
Il pannello di prova font arriva da claudehud_fonttest.res (#base): togliere la riga per spegnerlo.
Generato da tools/hand/gen_mainmenu.py""")
# prepend the #base include for the font test card
p = os.path.join(ROOT, "resource/ui/mainmenuoverride.res")
txt = open(p, encoding="utf-8").read()
lines = txt.split("\n")
i = next(k for k, l in enumerate(lines) if not l.startswith("//"))
lines.insert(i, '#base "claudehud_fonttest.res"')
open(p, "w", encoding="utf-8", newline="\n").write("\n".join(lines))

# ---------------------------------------------------------------- matchmaking top bar
T = ("TopBar",)
patch("resource/ui/matchmakingdashboard.res", {
    T + ("Gradient",): dict(HIDE, image=""),
    T + ("BGPanel",): {"bgcolor_override": "LtCard"},
    T + ("ToggleChatButton",): ICON_BTN,
    T + ("FindAGameButton",): light_btn(primary=True),
    T + ("ResumeButton",): light_btn(),
    T + ("QuitButton",): light_btn(),
    T + ("DisconnectButton",): light_btn(),
    T + ("QueueContainer", "BGPanel"): {"bgcolor_override": "LtCardAlt"},
    T + ("QueueContainer", "QueueText"): {"font": "TypeBodyStrong", "fgcolor_override": "LtText"},
    T + ("JoinPartyLobbyContainer", "BGPanel"): {"bgcolor_override": "LtCardAlt"},
    T + ("JoinPartyLobbyContainer", "JoinNowButton"): light_btn(primary=True, icon=False),
}, header="""ClaudeHUD: riscritto a mano (fase 6) - barra superiore del matchmaking (menu principale).
Striscia bianca, "Trova una partita" e' il bottone primario Ink (hover Terracotta), gli altri bottoni
sono secondari Pampas. Generato da tools/hand/gen_mainmenu.py""")
print("ok")
