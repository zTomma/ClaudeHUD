#!/usr/bin/env python3
"""
Hand layout for scripts/hudlayout.res (phases 3, 4, 7). Applied on top of the token migration of
Valve's original, then the file is marked as hand-written (tools/migrate.py stops touching it).
Geometry follows DESIGN.md par. 5: edge 12, combat cards 36 tall on the bottom rail (r12).
"""
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.dirname(HERE))
import migrate as M, modes, tokens as T, vdf

def lit(role):
    return T.rgba_str(role), "token: " + role

SET = {
    # bottom rail, right: ammo card; class meters stack above it, item meters to its left
    "HudWeaponAmmo":        {"xpos": "r100", "ypos": "r48", "wide": "92", "tall": "40"},
    "HudMedicCharge":       {"xpos": "r100", "ypos": "r88", "wide": "92", "tall": "40"},
    "HudDemomanCharge":     {"xpos": "r100", "ypos": "r56", "wide": "88", "tall": "4"},
    "HudBowCharge":         {"xpos": "r100", "ypos": "r56", "wide": "88", "tall": "4"},
    "HudFlameRocketCharge": {"xpos": "r100", "ypos": "r56", "wide": "88", "tall": "4"},
    "HudItemEffectMeter":   {"xpos": "r184", "ypos": "r48", "wide": "84", "tall": "40"},
    "HudDemomanPipes":      {"xpos": "r184", "ypos": "r48", "wide": "84", "tall": "40"},
    "CHealthAccountPanel":  {"xpos": "12", "ypos": "r192"},
    # killfeed: top right, 12 from the edges
    "HudDeathNotice": {"xpos": "r640", "ypos": "12", "wide": "628", "tall": "112",
                       "MaxDeathNotices": "5", "IconScale": "0.35", "LineHeight": "16", "LineSpacing": "4",
                       "CornerRadius": "3", "RightJustify": "1", "TextFont": "TypeBodyStrong",
                       "TeamBlue": "DkBluText", "TeamRed": "DkRedText", "IconColor": "DkText",
                       "LocalPlayerColor": "DkText",
                       "BaseBackgroundColor": "DkCard", "LocalBackgroundColor": "DkCardLocal",
                       "KillStreakBackgroundColor": "DkChip"},
    # left column, bottom to top: health block r76-r12, carrying weapon r108, spy disguise r144, chat r272
    "HudChat": {"xpos": "12", "ypos": "r272", "wide": "280", "tall": "120"},
    # target IDs: below the crosshair, outside the central rectangle
    # the code resizes the ROOT to the content (SetSize) and draws TargetIDBG at tf_hud_target_id_alpha
    # (default 100 = 39%): the opaque rounded card is therefore the root's own background
    "CMainTargetID":      {"ypos": "360", "tall": "30", "paintbackground": "1", "paintbackgroundtype": "2", "bgcolor_override": "DkCard"},
    "CSpectatorTargetID": {"ypos": "250", "tall": "30", "paintbackground": "1", "paintbackgroundtype": "2", "bgcolor_override": "DkCard"},
    "CSecondaryTargetID": {"ypos": "326", "tall": "30", "paintbackground": "1", "paintbackgroundtype": "2", "bgcolor_override": "DkCard"},
    # engineer metal card above the ammo card (inner card at x5 y103 in hudaccountpanel.res)
    "CHudAccountPanel":   {"xpos": "r105", "ypos": "r191", "wide": "100", "tall": "180"},
    # KOTH timers: two 80-wide cards, 4 apart, centred; the code moves ActiveTimerBG under the active one
    "HudKothTimeStatus": {"xpos": "c-82", "ypos": "0", "wide": "168", "tall": "64",
                          "blue_active_xpos": "0", "red_active_xpos": "84"},
    # spy disguise text: above the health block
    "DisguiseStatus": {"xpos": "12", "ypos": "r144", "wide": "180", "tall": "34", "TextFont": "TypeBodyStrong"},
}
DROP = re.compile(r"_(minmode|lodef|hidef)$", re.I)

CROSSHAIR = '''
	// Mirino ClaudeHUD (spento di default): un punto avorio su un quadrato DkCard, leggibile su
	// qualsiasi sfondo. Per usarlo: "visible" "1" sui due elementi e "crosshair 0" in console.
	"ClaudeXhairBack"
	{
		"ControlName"	"ImagePanel"
		"fieldName"		"ClaudeXhairBack"
		"xpos"			"c-2"
		"ypos"			"c-2"
		"zpos"			"1"
		"wide"			"4"
		"tall"			"4"
		"visible"		"0"
		"enabled"		"1"
		"fillcolor"		"%s"	// token: DkCard
	}
	"ClaudeXhairDot"
	{
		"ControlName"	"ImagePanel"
		"fieldName"		"ClaudeXhairDot"
		"xpos"			"c-1"
		"ypos"			"c-1"
		"zpos"			"2"
		"wide"			"2"
		"tall"			"2"
		"visible"		"0"
		"enabled"		"1"
		"fillcolor"		"%s"	// token: DkText
	}
''' % (T.rgba_str("DkCard"), T.rgba_str("DkText"))

def main():
    rel = "scripts/hudlayout.res"
    nodes = vdf.parse(open(os.path.join(ROOT, "#TF2 Files", rel), encoding="utf-8", errors="replace").read())
    ctx = M.load_ctx()
    M.migrate_nodes(nodes, "dark", ctx)
    root = nodes[0][1]
    for el in root:
        name, body = el[0], el[1]
        if name not in SET or not isinstance(body, list):
            continue
        body[:] = [nd for nd in body if not DROP.search(nd[0]) and not (nd[2] and "X360" in nd[2])]
        for nd in body:
            nd[2] = None if nd[2] and "WIN32" in nd[2] else nd[2]
        for k, v in SET[name].items():
            val, cm = (v if isinstance(v, tuple) else (v, None))
            hit = False
            for nd in body:
                if nd[0].lower() == k.lower():
                    nd[1], nd[3], hit = val, cm, True
            if not hit:
                body.append([k, val, None, cm])
    text = vdf.dump(nodes)
    text = text.rstrip()
    assert text.endswith("}")
    text = text[:-1].rstrip() + "\n" + CROSSHAIR + "}\n"
    head = ("// ClaudeHUD: riscritto a mano (fasi 3, 4, 7) - posizioni degli elementi HUD.\n"
            "// Colori migrati ai token; geometria: DESIGN.md par. 5 (bordo 12, binario inferiore r12, schede alte 36).\n"
            "// Generato da tools/hand/patch_hudlayout.py sull'originale Valve.\n")
    out = head + text
    vdf.parse(out)
    open(os.path.join(ROOT, rel), "w", encoding="utf-8", newline="\n").write(out)
    print("ok")

main()
