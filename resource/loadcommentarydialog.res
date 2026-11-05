// ClaudeHUD: migrato ai token (layout originale) - generato da tools/migrate.py
// modalita': light (DESIGN.md par. 9)
"resource/LoadCommentaryDialog.res"
{
	"LoadCommentaryDialog"
	{
		"ControlName"        	"CLoadGameDialog"
		"fieldName"          	"LoadCommentaryDialog"
		"xpos"               	"272"
		"ypos"               	"154"
		"wide"               	"480"
		"tall"               	"460"
		"autoResize"         	"0"
		"pinCorner"          	"0"
		"visible"            	"1"
		"enabled"            	"1"
		"tabPosition"        	"0"
		"settitlebarvisible" 	"1"
		"title"              	"#GameUI_LoadCommentary"
	}
	"listpanel_commentary"
	{
		"ControlName" 	"PanelListPanel"
		"fieldName"   	"listpanel_commentary"
		"xpos"        	"20"
		"ypos"        	"61"
		"wide"        	"444"
		"tall"        	"354"
		"autoResize"  	"3"
		"pinCorner"   	"0"
		"visible"     	"1"
		"enabled"     	"1"
		"tabPosition" 	"1"
	}
	"loadcommentary"
	{
		"ControlName"               	"Button"
		"fieldName"                 	"loadcommentary"
		"xpos"                      	"302"
		"ypos"                      	"422"
		"wide"                      	"82"
		"tall"                      	"24"
		"autoResize"                	"0"
		"pinCorner"                 	"3"
		"visible"                   	"1"
		"enabled"                   	"0"
		"tabPosition"               	"2"
		"labelText"                 	"#GameUI_Load"
		"textAlignment"             	"west"
		"dulltext"                  	"0"
		"brighttext"                	"0"
		"wrap"                      	"0"
		"Command"                   	"loadcommentary"
		"Default"                   	"1"
		"defaultFgColor_override"   	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
		"armedFgColor_override"     	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"depressedFgColor_override" 	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"defaultBgColor_override"   	"LtCardAlt"	// ClaudeHUD: colore esplicito in modalita' chiara
		"armedBgColor_override"     	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"depressedBgColor_override" 	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"Cancel"
	{
		"ControlName"               	"Button"
		"fieldName"                 	"Cancel"
		"xpos"                      	"394"
		"ypos"                      	"422"
		"wide"                      	"70"
		"tall"                      	"24"
		"autoResize"                	"0"
		"pinCorner"                 	"3"
		"visible"                   	"1"
		"enabled"                   	"1"
		"tabPosition"               	"3"
		"labelText"                 	"#GameUI_Cancel"
		"textAlignment"             	"west"
		"dulltext"                  	"0"
		"brighttext"                	"0"
		"wrap"                      	"0"
		"Command"                   	"Close"
		"Default"                   	"0"
		"defaultFgColor_override"   	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
		"armedFgColor_override"     	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"depressedFgColor_override" 	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"defaultBgColor_override"   	"LtCardAlt"	// ClaudeHUD: colore esplicito in modalita' chiara
		"armedBgColor_override"     	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"depressedBgColor_override" 	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"HelpText"
	{
		"ControlName"      	"Label"
		"fieldName"        	"HelpText"
		"xpos"             	"20"
		"ypos"             	"26"
		"wide"             	"444"
		"tall"             	"36"
		"autoResize"       	"0"
		"pinCorner"        	"0"
		"visible"          	"1"
		"enabled"          	"1"
		"tabPosition"      	"0"
		"labelText"        	"#GameUI_LoadCommentaryHelp"
		"textAlignment"    	"west"
		"dulltext"         	"0"
		"brighttext"       	"0"
		"wrap"             	"1"
		"fgcolor_override" 	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"topHorizLeft"
	{
		"ControlName"      	"Label"
		"fieldName"        	"topHorizLeft"
		"xpos"             	"0"
		"ypos"             	"0"
		"wide"             	"64"
		"tall"             	"24"
		"autoResize"       	"0"
		"pinCorner"        	"0"
		"visible"          	"0"
		"enabled"          	"1"
		"tabPosition"      	"0"
		"labelText"        	"Label"
		"textAlignment"    	"west"
		"dulltext"         	"0"
		"brighttext"       	"0"
		"wrap"             	"0"
		"fgcolor_override" 	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"topVertLeft"
	{
		"ControlName"      	"Label"
		"fieldName"        	"topVertLeft"
		"xpos"             	"0"
		"ypos"             	"0"
		"wide"             	"64"
		"tall"             	"24"
		"autoResize"       	"0"
		"pinCorner"        	"0"
		"visible"          	"0"
		"enabled"          	"1"
		"tabPosition"      	"0"
		"labelText"        	"Label"
		"textAlignment"    	"west"
		"dulltext"         	"0"
		"brighttext"       	"0"
		"wrap"             	"0"
		"fgcolor_override" 	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"bottomHorizRight"
	{
		"ControlName"      	"Label"
		"fieldName"        	"bottomHorizRight"
		"xpos"             	"0"
		"ypos"             	"0"
		"wide"             	"64"
		"tall"             	"24"
		"autoResize"       	"0"
		"pinCorner"        	"0"
		"visible"          	"0"
		"enabled"          	"1"
		"tabPosition"      	"0"
		"labelText"        	"Label"
		"textAlignment"    	"west"
		"dulltext"         	"0"
		"brighttext"       	"0"
		"wrap"             	"0"
		"fgcolor_override" 	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"bottomVertRight"
	{
		"ControlName"      	"Label"
		"fieldName"        	"bottomVertRight"
		"xpos"             	"0"
		"ypos"             	"0"
		"wide"             	"64"
		"tall"             	"24"
		"autoResize"       	"0"
		"pinCorner"        	"0"
		"visible"          	"0"
		"enabled"          	"1"
		"tabPosition"      	"0"
		"labelText"        	"Label"
		"textAlignment"    	"west"
		"dulltext"         	"0"
		"brighttext"       	"0"
		"wrap"             	"0"
		"fgcolor_override" 	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
}
