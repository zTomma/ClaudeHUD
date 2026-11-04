"""
Mode assignment (DESIGN.md §9): which surfaces use the dark in-game variant and which the
light editorial variant.

Rule: dark where the match or the game's items are; light where you navigate and read.
Item surfaces stay dark because TF2's quality/rarity colours (Unique yellow, Unusual
purple, ...) are game semantics calibrated for dark backgrounds.
"""
import fnmatch

LIGHT = [
    # main menu and its satellites
    "resource/gamemenu.res", "resource/gamelogo.res",
    "resource/ui/mainmenu*.res",
    "resource/ui/streamlistpanel.res", "resource/ui/streampanel.res",
    "resource/ui/badgepanel.res", "resource/ui/staticbadgepanel.res",
    "resource/ui/xpsourcepanel.res", "resource/ui/navigationpaneltest.res",
    # class / team / map / MOTD (pause screens)
    "resource/ui/classselection*.res", "resource/ui/classmenu.res", "resource/ui/classtips*.res",
    "resource/ui/teammenu*.res", "resource/ui/hudarenateammenu*.res",
    "resource/ui/intromenu*.res", "resource/ui/mapinfomenu*.res", "resource/ui/textwindow*.res",
    # scoreboards
    "resource/ui/scoreboard.res", "resource/ui/mvmscoreboard*.res",
    # matchmaking, lobby, ranks, stats
    "resource/ui/matchmaking*.res", "resource/ui/lobby*.res", "resource/ui/quickplay*.res",
    "resource/ui/casual*.res", "resource/ui/competitive*.res", "resource/ui/comprank*.res",
    "resource/ui/pvp*.res", "resource/ui/compstats.res", "resource/ui/matchhistoryentrypanel.res",
    "resource/ui/leaderboard*.res", "resource/ui/dashboardpartymember.res",
    "resource/ui/playlistentry*.res", "resource/ui/mmissuedialog.res",
    # dialogs opened from the menus
    "resource/ui/confirmabandondialog.res", "resource/ui/abusereportsubmitdialog.res",
    "resource/ui/cheatdetectiondialog.res", "resource/ui/selectplayerdialog*.res",
    "resource/ui/selectmosthelpfulfrienddialog.res", "resource/ui/steamworkshopdialog.res",
    "resource/ui/publish*.res", "resource/ui/import*.res", "resource/ui/supportnotificationdialog.res",
    "resource/ui/servernotconnectedtosteam.res", "resource/ui/surveypanel*.res",
    "resource/ui/tfadvancedoptionsdialog.res", "resource/ui/achievementsdialog.res",
    "resource/ui/statsummary*.res", "resource/ui/training*.res",
    "resource/ui/training/*/*.res", "resource/ui/videopanel.res", "resource/ui/explanationpopup.res",
    "resource/ui/globalexplanations.res", "resource/ui/xboxdialogs.res", "resource/ui/vrcalibration.res",
    "resource/ui/saxxyawards_submitform.res", "resource/ui/steamfriendpanel.res",
    "resource/ui/invitenotification.res",
    # GameUI dialogs living in resource/
    "resource/commentary*.res", "resource/createofflinepracticepage.res", "resource/loadcommentarydialog.res",
    "resource/loadingdialog*.res", "resource/muteplayerdialog.res", "resource/newgame*.res",
    "resource/offline_practice.res", "resource/optionssubmultiplayer.res", "resource/playerlistdialog.res",
    "resource/reportplayerdialog.res", "resource/training.res", "resource/sourcescheme.res",
]

REFERENCE_PREFIXES = ("#tf2 files/", "#hl2 files/", "#platform files/", "#map files/")


def mode_of(path):
    p = path.replace("\\", "/").lower().lstrip("./")
    if p.startswith(REFERENCE_PREFIXES):
        return "ref"
    for pat in LIGHT:
        if fnmatch.fnmatch(p, pat):
            return "light"
    return "dark"
