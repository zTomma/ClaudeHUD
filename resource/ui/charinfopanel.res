// ClaudeHUD: migrato ai token (layout originale) - generato da tools/migrate.py
// modalita': dark (DESIGN.md par. 9)
"Resource/UI/CharInfoPanel.res"
{
	"character_info"
	{
		"ControlName"                      	"EditablePanel"
		"fieldName"                        	"character_info"
		"xpos"                             	"0"
		"ypos"                             	"0"
		"wide"                             	"f0"
		"tall"                             	"480"
		"autoResize"                       	"0"
		"pinCorner"                        	"0"
		"visible"                          	"1"
		"enabled"                          	"1"
		"tabPosition"                      	"0"
		"settitlebarvisible"               	"1"
		"PaintBackgroundType"              	"0"
		"bgcolor_override"                 	"Clear"
		"infocus_bgcolor_override"         	"20 20 19 0"	// token: Clear
		"outoffocus_bgcolor_override"      	"20 20 19 0"	// token: Clear
		"title"                            	"#CharInfoAndSetup"
		"title_font"                       	"HudFontMediumBold"
		"titletextinsetX"                  	"40"
		"titletextinsetY"                  	"0"
		"titlebarfgcolor_override"         	"250 249 245 255"	// token: DkText
		"titlebardisabledfgcolor_override" 	"250 249 245 255"	// token: DkText
		"titlebarbgcolor_override"         	"39 38 36 255"	// token: DkCard
		"clientinsetx_override"            	"0"
		"sheetinset_bottom"                	"40"
	}
	"BackgroundHeader"
	{
		"ControlName" 	"ImagePanel"
		"fieldName"   	"BackgroundHeader"
		"xpos"        	"0"
		"ypos"        	"0"
		"zpos"        	"-2"
		"wide"        	"f0"
		"tall"        	"120"
		"visible"     	"1"
		"enabled"     	"1"
		"image"       	"loadout_header"
		"tileImage"   	"1"
	}
	"BackgroundFooter"
	{
		"ControlName" 	"ImagePanel"
		"fieldName"   	"BackgroundFooter"
		"xpos"        	"0"
		"ypos"        	"420"
		"zpos"        	"1"
		"wide"        	"f0"
		"tall"        	"60"
		"visible"     	"1"
		"enabled"     	"1"
		"image"       	"loadout_bottom_gradient"
		"tileImage"   	"1"
	}
	"FooterLine"
	{
		"ControlName" 	"ImagePanel"
		"fieldName"   	"FooterLine"
		"xpos"        	"0"
		"ypos"        	"420"
		"zpos"        	"2"
		"wide"        	"f0"
		"tall"        	"10"
		"visible"     	"1"
		"enabled"     	"1"
		"image"       	"loadout_solid_line"
		"scaleImage"  	"1"
	}
	"Sheet"
	{
		"ControlName"     	"EditablePanel"
		"fieldName"       	"Sheet"
		"tabxindent"      	"80"
		"tabxdelta"       	"10"
		"tabwidth"        	"240"
		"tabheight"       	"20"
		"transition_time" 	"0"
		"yoffset"         	"14"
		"HeaderLine"
		{
			"ControlName" 	"ImagePanel"
			"fieldName"   	"HeaderLine"
			"xpos"        	"0"
			"ypos"        	"32"
			"zpos"        	"5"
			"wide"        	"f0"
			"tall"        	"10"
			"visible"     	"1"
			"enabled"     	"1"
			"image"       	"loadout_solid_line"
			"scaleImage"  	"1"
		}
		"tabskv"
		{
			"textinsetx"              	"40"
			"font"                    	"HudFontMediumSmallBold"
			"selectedcolor"           	"250 249 245 255"	// token: DkText
			"unselectedcolor"         	"177 173 161 255"	// token: DkTextMuted
			"defaultBgColor_override" 	"DkCard"
			"paintbackground"         	"0"
			"activeborder_override"   	"OutlinedGreyBox"
			"normalborder_override"   	"OutlinedDullGreyBox"
		}
	}
	"BackButton"
	{
		"ControlName"     	"CExButton"
		"fieldName"       	"BackButton"
		"xpos"            	"c-295"
		"ypos"            	"437"
		"zpos"            	"2"
		"wide"            	"100"
		"tall"            	"25"
		"autoResize"      	"0"
		"pinCorner"       	"3"
		"visible"         	"1"
		"enabled"         	"1"
		"tabPosition"     	"0"
		"labelText"       	"#TF_BackCarat"
		"font"            	"HudFontSmallBold"
		"textAlignment"   	"center"
		"dulltext"        	"0"
		"brighttext"      	"0"
		"default"         	"0"
		"Command"         	"back"
		"sound_depressed" 	"UI/buttonclick.wav"
		"sound_released"  	"UI/buttonclickrelease.wav"
	}
	"NotificationsPresentPanel"
	{
		"ControlName" 	"CNotificationsPresentPanel"
		"fieldName"   	"NotificationsPresentPanel"
		"xpos"        	"r200"
		"ypos"        	"10"
		"zpos"        	"10000"
		"wide"        	"190"
		"tall"        	"50"
		"visible"     	"0"
		"enabled"     	"1"
	}
}
