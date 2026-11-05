// ClaudeHUD: migrato ai token (layout originale) - generato da tools/migrate.py
// modalita': dark (DESIGN.md par. 9)
"Resource/UI/GenericNotificationToast.res"
{
	"GenericNotificationToast"
	{
		"ControlName"      	"CGenericNotificationToast"
		"fieldName"        	"GenericNotificationToast"
		"xpos"             	"0"
		"ypos"             	"0"
		"zpos"             	"1"
		"wide"             	"150"
		"tall"             	"50"
		"visible"          	"1"
		"enabled"          	"1"
		"fgcolor"          	"20 20 19 255"	// token: DkOnRed
		"fgcolor_override" 	"DkOnRed"
	}
	"AvatarBGPanel"
	{
		"ControlName"         	"EditablePanel"
		"fieldName"           	"AvatarBGPanel"
		"xpos"                	"7"
		"ypos"                	"7"
		"zpos"                	"-1"
		"wide"                	"36"
		"tall"                	"36"
		"visible"             	"1"
		"PaintBackgroundType" 	"2"
		"bgcolor_override"    	"DkChip"
	}
	"AvatarImage"
	{
		"ControlName"   	"CAvatarImagePanel"
		"fieldName"     	"AvatarImage"
		"xpos"          	"9"
		"ypos"          	"9"
		"zpos"          	"0"
		"wide"          	"32"
		"tall"          	"32"
		"visible"       	"1"
		"enabled"       	"1"
		"image"         	""
		"scaleImage"    	"1"
		"color_outline" 	"20 20 19 255"	// token: DkOnRed
	}
	"AvatarTextLabel"
	{
		"ControlName"      	"CExLabel"
		"fieldName"        	"AvatarTextLabel"
		"fgcolor"          	"DkOnRed"
		"fgcolor_override" 	"DkOnRed"
		"xpos"             	"45"
		"ypos"             	"7"
		"zpos"             	"2"
		"wide"             	"100"
		"tall"             	"38"
		"autoResize"       	"0"
		"pinCorner"        	"0"
		"visible"          	"0"
		"enabled"          	"1"
		"wrap"             	"1"
		"labelText"        	"%avatartext%"
		"textAlignment"    	"West"
		"font"             	"HudFontSmallest"
	}
	"TextLabel"
	{
		"ControlName"      	"CExLabel"
		"fieldName"        	"TextLabel"
		"fgcolor"          	"DkOnRed"
		"fgcolor_override" 	"DkOnRed"
		"if_high_priority"
		{
			"fgcolor"          	"217 119 87 255"	// token: DkAccent
			"fgcolor_override" 	"DkAccent"
			"font"             	"StorePromotionsTitle"
		}
		"xpos"             	"7"
		"ypos"             	"7"
		"zpos"             	"2"
		"wide"             	"138"
		"tall"             	"38"
		"autoResize"       	"0"
		"pinCorner"        	"0"
		"visible"          	"0"
		"enabled"          	"1"
		"wrap"             	"1"
		"labelText"        	"%text%"
		"textAlignment"    	"West"
		"font"             	"HudFontSmallest"
	}
}
