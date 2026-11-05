// ClaudeHUD: migrato ai token (layout originale) - generato da tools/migrate.py
// modalita': light (DESIGN.md par. 9)
"Resource/UI/MatchmakingGroupPanel.res"
{
	"MatchmakingGroupPanel"
	{
		"fieldName"            	"ScrollableImageListEntry"
		"xpos"                 	"0"
		"ypos"                 	"0"
		"wide"                 	"f0"
		"tall"                 	"25"
		"proportionaltoparent" 	"1"
	}
	"BGPanel"
	{
		"fieldName"            	"BGPanel"
		"ControlName"          	"EditablePanel"
		"xpos"                 	"cs-0.5"
		"ypos"                 	"0"
		"wide"                 	"p1.3"
		"tall"                 	"f0"
		"proportionaltoparent" 	"1"
		"border"               	"MainMenuBGBorder"
		"bgcolor_override"     	"LtCard"	// ClaudeHUD: riempimento al posto del bordo texture
	}
	"Checkbutton"
	{
		"ControlName"            	"CExCheckButton"
		"fieldName"              	"Checkbutton"
		"xpos"                   	"0"
		"ypos"                   	"2"
		"zpos"                   	"3"
		"wide"                   	"f0"
		"tall"                   	"20"
		"proportionaltoparent"   	"1"
		"labeltext"              	""
		"smallcheckimage"        	"1"
		"fgcolor"                	"20 20 19 255"	// token: LtText
		"font"                   	"HudFontSmallBold"
		"sound_depressed"        	"UI/buttonclickrelease.wav"
		"button_activation_type" 	"1"
		"fgcolor_override"       	"LtText"	// ClaudeHUD: contrasto nel contesto
	}
}
