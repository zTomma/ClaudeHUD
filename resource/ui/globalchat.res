// ClaudeHUD: migrato ai token (layout originale) - generato da tools/migrate.py
// modalita': dark (DESIGN.md par. 9)
"Resource/UI/GlobalChat.res"
{
	"partychat"
	{
		"fieldName"                   	"partychat"
		"visible"                     	"1"
		"enabled"                     	"1"
		"xpos"                        	"5"
		"ypos"                        	"10"
		"zpos"                        	"1001"
		"wide"                        	"200"
		"tall"                        	"200"
		"proportionaltoparent"        	"1"
		"keyboardinputenabled"        	"1"
		"mouseinputenabled"           	"1"
		"border"                      	"QuickplayBorder"
		"log_font_small"              	"HudFontSmallest"
		"log_font_medium"             	"HudFontSmallest"
		"log_font_large"              	"HudFontSmallest"
		"chat_color_default"          	"250 249 245 255"	// token: DkText
		"chat_color_player_name"      	"217 119 87 255"	// token: DkAccent
		"chat_color_chat_text"        	"250 249 245 255"	// token: DkText
		"chat_color_party_event"      	"Orange"
		"collapsed_height"            	"0"
		"expanded_height"             	"200"
		"resize_time"                 	"0.3"
		"invalidate_parent_on_resize" 	"0"
		"bgcolor_override"            	"DkCard"	// ClaudeHUD: riempimento al posto del bordo texture
	}
	"chatlog"
	{
		"fieldName"            	"chatlog"
		"xpos"                 	"cs-0.5"
		"ypos"                 	"5"
		"zpos"                 	"1"
		"wide"                 	"f0"
		"tall"                 	"f20"
		"visible"              	"1"
		"proportionaltoparent" 	"1"
		"RoundedCorners"       	"0"
		"font"                 	"HudFontSmallest"
		"bgcolor_override"     	"DkCardA20"
		"pinCorner"            	"2"
		"autoResize"           	"1"
		"ScrollBar"
		{
			"FieldName"            	"ScrollBar"
			"xpos"                 	"rs1-1"
			"ypos"                 	"0"
			"tall"                 	"f0"
			"wide"                 	"5"	// This gets slammed from client schme.  GG.
			"zpos"                 	"1000"
			"nobuttons"            	"1"
			"proportionaltoparent" 	"1"
			"Slider"
			{
				"fgcolor_override" 	"DkText"
			}
			"UpButton"
			{
				"ControlName" 	"Button"
				"FieldName"   	"UpButton"
				"visible"     	"0"
			}
			"DownButton"
			{
				"ControlName" 	"Button"
				"FieldName"   	"DownButton"
				"visible"     	"0"
			}
		}
	}
	"chatentry"
	{
		"fieldName"            	"chatentry"
		"xpos"                 	"6"
		"ypos"                 	"rs1+19"
		"zpos"                 	"1"
		"wide"                 	"f2"
		"tall"                 	"13"
		"visible"              	"1"
		"proportionaltoparent" 	"1"
		"bgcolor_override"     	"DkCard"
		"RoundedCorners"       	"0"
		"font"                 	"HudFontSmallest"
		"alpha"                	"0"
		"mouseinputenabled"    	"0"
		"pinCorner"            	"2"
	}
	"EntryShadow"
	{
		"ControlName"          	"Panel"
		"fieldName"            	"EntryShadow"
		"xpos"                 	"cs-0.5"
		"ypos"                 	"rs1"
		"zpos"                 	"2"
		"wide"                 	"f0"
		"tall"                 	"15"
		"visible"              	"1"
		"proportionaltoparent" 	"1"
		"bgcolor_override"     	"Clear"
		"RoundedCorners"       	"0"
		"border"               	"QuickplayBorder"
		"keyboardinputenabled" 	"0"
		"mouseinputenabled"    	"0"
		"pinCorner"            	"2"
	}
}
