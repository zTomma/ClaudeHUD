#!/usr/bin/env python3
"""resource/ui/hudmatchstatus.res: round timer card position + countdown typography."""
from _patch import patch, lit
patch("resource/ui/hudmatchstatus.res", {
    ("ObjectiveStatusTimePanel",): {"xpos": "c-40", "ypos": "8", "wide": "84", "tall": "52"},
    ("ObjectiveStatusTimePanel", "TimePanelValue"): {"xpos": "2", "ypos": "0", "wide": "60", "tall": "28",
                                                     "font": "NumL", "fgcolor": "DkText", "textAlignment": "center"},
    ("CountdownLabel",): {"font": "NumXL", "fgcolor": "DkText"},
    ("CountdownLabelShadow",): {"font": "NumXL", "fgcolor": "Clear", "wide": "0", "tall": "0"},
    ("RankUpLabel",): {"font": "TypeBodyStrong", "fgcolor": "DkText"},
    ("RankUpShadowLabel",): {"font": "TypeBodyStrong", "fgcolor": "Clear", "wide": "0", "tall": "0"},
}, header="""ClaudeHUD: riscritto a mano (fase 4) - stato della partita: posizione e tipografia del timer
(scheda 80x28 in alto al centro, NumL), conto alla rovescia in NumXL, ombre trasparenti.
Il resto (squadre, giocatori) resta nel layout originale con i colori migrati ai token.
Generato da tools/hand/gen_matchstatus.py""")
print("ok")
