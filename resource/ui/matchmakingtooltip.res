// ClaudeHUD: migrato ai token (layout originale) - generato da tools/migrate.py
// modalita': light (DESIGN.md par. 9)
"Resource/UI/MatchMakingTooltip.res"
{
	"TooltipPanel"
	{
		"fieldName"           	"TooltipPanel"
		"xpos"                	"0"
		"ypos"                	"0"
		"zpos"                	"30000"
		"wide"                	"300"
		"tall"                	"100"
		"visible"             	"0"
		"PaintBackgroundType" 	"2"
		"border"              	"MainMenuBGBorder"
		"mouseinputenabled"   	"0"
		"TipLabel"
		{
			"ControlName"          	"CExLabel"
			"fieldName"            	"TipLabel"
			"if_small"
			{
				"font" 	"FontStoreOriginalPrice"
			}
			"if_medium"
			{
				"font" 	"HudFontSmall"
			}
			"if_large"
			{
				"font" 	"HudFontSmallBold"
			}
			"labelText"            	"%tiptext%"
			"textAlignment"        	"center"
			"xpos"                 	"10"
			"ypos"                 	"10"
			"zpos"                 	"2"
			"wide"                 	"140"
			"tall"                 	"30"
			"autoResize"           	"0"
			"pinCorner"            	"0"
			"visible"              	"1"
			"enabled"              	"1"
			"fgcolor_override"     	"LtText"
			"auto_wide_tocontents" 	"1"
			"auto_tall_tocontents" 	"1"
			"centerwrap"           	"1"
		}
		"bgcolor_override"    	"LtCard"	// ClaudeHUD: riempimento al posto del bordo texture
	}
}
