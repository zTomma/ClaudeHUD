// ClaudeHUD: migrato ai token (layout originale) - generato da tools/migrate.py
// modalita': light (DESIGN.md par. 9)
"resource/ListThumbnail.res"
{
	"ListThumbnail"
	{
		"ControlName" 	"Panel"
		"fieldName"   	"ListThumbnail"
		"wide"        	"88"
		"tall"        	"74"
		"autoResize"  	"0"
		"pinCorner"   	"0"
		"enabled"     	"1"
	}
	"BorderPanel"
	{
		"ControlName"      	"EditablePanel"
		"FieldName"        	"BorderPanel"
		"xpos"             	"0"
		"ypos"             	"0"
		"zpos"             	"0"
		"wide"             	"88"
		"tall"             	"54"
		"autoresize"       	"0"
		"pincorner"        	"0"
		"visible"          	"1"
		"enabled"          	"1"
		"border"           	"ReplayDefaultBorder"
		"bgcolor_override" 	"LtCard"	// ClaudeHUD: riempimento al posto del bordo texture
	}
	"ScreenshotThumbnail"
	{
		"ControlName" 	"Panel"
		"fieldName"   	"ScreenshotThumbnail"
		"xpos"        	"2"
		"ypos"        	"2"
		"zpos"        	"1"
		"wide"        	"84"
		"tall"        	"50"
		"autoResize"  	"0"
		"pinCorner"   	"0"
	}
	"DownloadProgress"
	{
		"ControlName"      	"ProgressBar"
		"fieldName"        	"DownloadProgress"
		"zpos"             	"3"
		"autoResize"       	"0"
		"pinCorner"        	"0"
		"visible"          	"0"
		"tall"             	"10"
		"enabled"          	"1"
		"bgcolor_override" 	"LtCardAlt"
		"fgcolor_override" 	"LtText"
	}
	"RecordingInProgressLabel"
	{
		"ControlName"      	"CExLabel"
		"fieldName"        	"RecordingInProgressLabel"
		"font"             	"ReplayMediumSmall"
		"labelText"        	"#Replay_RecordingInProgress"
		"textAlignment"    	"west"
		"zpos"             	"3"
		"autoResize"       	"0"
		"pinCorner"        	"0"
		"visible"          	"0"
		"enabled"          	"1"
		"centerwrap"       	"1"
		"paintbackground"  	"0"
		"fgcolor_override" 	"LtAccentText"
	}
	"DownloadLabel"
	{
		"ControlName"      	"CExLabel"
		"fieldName"        	"DownloadLabel"
		"font"             	"ReplayMediumSmall"
		"labelText"        	"#Replay_Connecting"
		"textAlignment"    	"west"
		"zpos"             	"3"
		"autoResize"       	"0"
		"pinCorner"        	"0"
		"visible"          	"1"
		"enabled"          	"1"
		"fgcolor_override" 	"LtText"
	}
	"ErrorLabel"
	{
		"ControlName"      	"CExLabel"
		"fieldName"        	"ErrorLabel"
		"font"             	"TypeHeading"
		"labelText"        	"#Replay_Error"
		"textAlignment"    	"west"
		"zpos"             	"3"
		"autoResize"       	"0"
		"pinCorner"        	"0"
		"visible"          	"0"
		"enabled"          	"1"
		"fgcolor_override" 	"LtAccentText"
	}
	"TitleLabel"
	{
		"ControlName"      	"CExLabel"
		"fieldName"        	"TitleLabel"
		"font"             	"DefaultVerySmall"
		"labelText"        	"Untitled"
		"textAlignment"    	"north-west"
		"xpos"             	"2"
		"ypos"             	"56"
		"wide"             	"76"
		"tall"             	"15"
		"zpos"             	"10"
		"autoResize"       	"0"
		"pinCorner"        	"0"
		"enabled"          	"1"
		"fgcolor_override" 	"LtText"
	}
	"DownloadButton"
	{
		"ControlName"               	"CExButton"
		"fieldName"                 	"DownloadButton"
		"xpos"                      	"0"
		"ypos"                      	"0"
		"zpos"                      	"10"
		"wide"                      	"40"
		"tall"                      	"40"
		"autoResize"                	"0"
		"pinCorner"                 	"0"
		"visible"                   	"0"
		"enabled"                   	"1"
		"tabPosition"               	"0"
		"labelText"                 	"#Replay_Download"
		"font"                      	"ReplayMediumSmall"
		"textAlignment"             	"center"
		"wrap"                      	"0"
		"Command"                   	"download"
		"defaultFgColor_override"   	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
		"armedFgColor_override"     	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"depressedFgColor_override" 	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"defaultBgColor_override"   	"LtCardAlt"	// ClaudeHUD: colore esplicito in modalita' chiara
		"armedBgColor_override"     	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"depressedBgColor_override" 	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"DownloadOverlay"
	{
		"ControlName"      	"Panel"
		"fieldName"        	"DownloadOverlay"
		"zpos"             	"2"
		"autoResize"       	"0"
		"pinCorner"        	"0"
		"visible"          	"0"
		"enabled"          	"1"
		"bgcolor_override" 	"LtCardAltA80"
		"Command"          	"overlay_clicked"
	}
	"DeleteButton"
	{
		"ControlName"               	"CExButton"
		"fieldName"                 	"DeleteButton"
		"xpos"                      	"70"
		"ypos"                      	"3"
		"zpos"                      	"10"
		"wide"                      	"15"
		"tall"                      	"15"
		"autoResize"                	"0"
		"pinCorner"                 	"0"
		"visible"                   	"0"
		"enabled"                   	"1"
		"tabPosition"               	"0"
		"labelText"                 	"X"
		"font"                      	"ReplayMediumSmall"
		"textAlignment"             	"center"
		"wrap"                      	"0"
		"Command"                   	"delete_replayitem"
		"fgcolor"                   	"LtAccentText"
		"defaultFgColor_override"   	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
		"armedFgColor_override"     	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"depressedFgColor_override" 	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"defaultBgColor_override"   	"LtCardAlt"	// ClaudeHUD: colore esplicito in modalita' chiara
		"armedBgColor_override"     	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"depressedBgColor_override" 	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
}
