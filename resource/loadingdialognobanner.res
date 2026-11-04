// ClaudeHUD: migrato ai token (layout originale) - generato da tools/migrate.py
// modalita': light (DESIGN.md par. 9)
"Resource/LoadingDialog.res"
{
	"LoadingDialog"
	{
		"ControlName" 	"Frame"
		"fieldName"   	"LoadingDialog"
		"xpos"        	"322"
		"ypos"        	"249"
		"wide"        	"380"
		"tall"        	"112"
		"autoResize"  	"0"
		"pinCorner"   	"0"
		"visible"     	"1"
		"enabled"     	"1"
		"tabPosition" 	"0"
	}
	"InfoLabel"
	{
		"ControlName"      	"Label"
		"fieldName"        	"InfoLabel"
		"xpos"             	"20"
		"ypos"             	"34"
		"wide"             	"340"
		"tall"             	"24"
		"autoResize"       	"0"
		"pinCorner"        	"0"
		"visible"          	"1"
		"enabled"          	"1"
		"tabPosition"      	"0"
		"labelText"        	"#GameUI_ParseBaseline"
		"textAlignment"    	"west"
		"dulltext"         	"1"
		"brighttext"       	"0"
		"fgcolor_override" 	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"progress"
	{
		"ControlName" 	"ProgressBar"
		"fieldName"   	"Progress"
		"xpos"        	"20"
		"ypos"        	"64"
		"wide"        	"260"
		"tall"        	"24"
		"autoResize"  	"0"
		"pinCorner"   	"0"
		"visible"     	"1"
		"enabled"     	"1"
		"tabPosition" 	"0"
	}
	"CancelButton"
	{
		"ControlName"               	"Button"
		"fieldName"                 	"CancelButton"
		"xpos"                      	"288"
		"ypos"                      	"64"
		"wide"                      	"72"
		"tall"                      	"24"
		"autoResize"                	"0"
		"pinCorner"                 	"0"
		"visible"                   	"1"
		"enabled"                   	"1"
		"tabPosition"               	"0"
		"labelText"                 	"#GameUI_Cancel"
		"textAlignment"             	"west"
		"dulltext"                  	"0"
		"brighttext"                	"0"
		"command"                   	"Cancel"
		"Default"                   	"0"
		"defaultFgColor_override"   	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
		"armedFgColor_override"     	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"depressedFgColor_override" 	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"defaultBgColor_override"   	"LtCardAlt"	// ClaudeHUD: colore esplicito in modalita' chiara
		"armedBgColor_override"     	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"depressedBgColor_override" 	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"Divider1"
	{
		"ControlName" 	"Divider"
		"fieldName"   	"Divider1"
		"xpos"        	"20"
		"ypos"        	"104"
		"wide"        	"340"
		"tall"        	"2"
		"autoResize"  	"0"
		"pinCorner"   	"0"
		"visible"     	"0"
		"enabled"     	"1"
		"tabPosition" 	"0"
	}
	"Label1"
	{
		"ControlName"      	"Label"
		"fieldName"        	"Label1"
		"xpos"             	"20"
		"ypos"             	"109"
		"wide"             	"340"
		"tall"             	"24"
		"autoResize"       	"0"
		"pinCorner"        	"0"
		"visible"          	"0"
		"enabled"          	"1"
		"tabPosition"      	"0"
		"labelText"        	"#GameUI_LoadingDialog_ContentHosting"
		"textAlignment"    	"west"
		"dulltext"         	"1"
		"brighttext"       	"0"
		"fgcolor_override" 	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"BannerAd"
	{
		"ControlName" 	"HTML"
		"fieldName"   	"BannerAd"
		"xpos"        	"20"
		"ypos"        	"136"
		"wide"        	"340"
		"tall"        	"56"
		"autoResize"  	"0"
		"pinCorner"   	"0"
		"visible"     	"0"
		"enabled"     	"1"
		"tabPosition" 	"0"
	}
}
