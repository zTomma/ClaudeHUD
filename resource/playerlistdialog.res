// ClaudeHUD: migrato ai token (layout originale) - generato da tools/migrate.py
// modalita': light (DESIGN.md par. 9)
"Resource/PlayerListDialog.res"
{
	"PlayerListDialog"
	{
		"ControlName"        	"CPlayerListDialog"
		"fieldName"          	"PlayerListDialog"
		"xpos"               	"168"
		"ypos"               	"55"
		"wide"               	"467"
		"tall"               	"388"
		"autoResize"         	"0"
		"pinCorner"          	"0"
		"visible"            	"1"
		"enabled"            	"1"
		"tabPosition"        	"0"
		"settitlebarvisible" 	"1"
	}
	"MuteButton"
	{
		"ControlName"               	"Button"
		"fieldName"                 	"MuteButton"
		"xpos"                      	"173"
		"ypos"                      	"326"
		"wide"                      	"144"
		"tall"                      	"24"
		"autoResize"                	"0"
		"pinCorner"                 	"2"
		"visible"                   	"1"
		"enabled"                   	"1"
		"tabPosition"               	"3"
		"labelText"                 	"#GameUI_MuteIngameVoice"
		"textAlignment"             	"west"
		"dulltext"                  	"0"
		"brighttext"                	"0"
		"Command"                   	"Mute"
		"Default"                   	"1"
		"defaultFgColor_override"   	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
		"armedFgColor_override"     	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"depressedFgColor_override" 	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"defaultBgColor_override"   	"LtCardAlt"	// ClaudeHUD: colore esplicito in modalita' chiara
		"armedBgColor_override"     	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"depressedBgColor_override" 	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"PlayerList"
	{
		"ControlName" 	"ListPanel"
		"fieldName"   	"PlayerList"
		"xpos"        	"28"
		"ypos"        	"38"
		"wide"        	"410"
		"tall"        	"279"
		"autoResize"  	"3"
		"pinCorner"   	"0"
		"visible"     	"1"
		"enabled"     	"1"
		"tabPosition" 	"1"
	}
	"Button1"
	{
		"ControlName"               	"Button"
		"fieldName"                 	"Button1"
		"xpos"                      	"352"
		"ypos"                      	"352"
		"wide"                      	"86"
		"tall"                      	"24"
		"autoResize"                	"0"
		"pinCorner"                 	"3"
		"visible"                   	"1"
		"enabled"                   	"1"
		"tabPosition"               	"4"
		"labelText"                 	"#GameUI_Close"
		"textAlignment"             	"west"
		"dulltext"                  	"0"
		"brighttext"                	"0"
		"Command"                   	"Close"
		"Default"                   	"0"
		"defaultFgColor_override"   	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
		"armedFgColor_override"     	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"depressedFgColor_override" 	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"defaultBgColor_override"   	"LtCardAlt"	// ClaudeHUD: colore esplicito in modalita' chiara
		"armedBgColor_override"     	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"depressedBgColor_override" 	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
}
