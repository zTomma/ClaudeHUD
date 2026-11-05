// ClaudeHUD: migrato ai token (layout originale) - generato da tools/migrate.py
// modalita': dark (DESIGN.md par. 9)
"Resource/UI/build_menu/base_selectable.res"
{
	"MainBackground"
	{
		"ControlName" 	"CIconPanel"
		"fieldName"   	"MainBackground"
		"xpos"        	"3"
		"ypos"        	"1"
		"zpos"        	"0"
		"wide"        	"98"
		"tall"        	"135"
		"visible"     	"1"
		"enabled"     	"1"
		"scaleImage"  	"1"
		"icon"        	"hud_menu_item_bg"
		"iconColor"   	"177 173 161 255"	// token: DkTextMuted
	}
	"ItemNameLabel"
	{
		"ControlName"     	"CExLabel"
		"fieldName"       	"ItemNameLabel"
		"font"            	"Default"
		"xpos"            	"10"
		"ypos"            	"2"
		"zpos"            	"1"
		"wide"            	"84"
		"tall"            	"15"
		"autoResize"      	"0"
		"pinCorner"       	"0"
		"visible"         	"1"
		"enabled"         	"1"
		"labelText"       	"#TF_Empty_Slot"
		"labelText_lodef" 	"#TF_Empty_Slot"
		"textAlignment"   	"Left"
		"dulltext"        	"0"
		"brighttext"      	"0"
		"fgcolor"         	"DkCard"
	}
	"ItemBackground"
	{
		"ControlName" 	"CIconPanel"
		"fieldName"   	"ItemBackground"
		"xpos"        	"4"
		"ypos"        	"0"
		"zpos"        	"0"
		"wide"        	"98"
		"tall"        	"135"
		"visible"     	"1"
		"enabled"     	"1"
		"scaleImage"  	"1"
		"icon"        	"hud_menu_item_bg"
		"iconColor"   	"20 20 19 255"	// token: DkOnRed
	}
	"BuildingIcon"
	{
		"ControlName" 	"CIconPanel"
		"fieldName"   	"BuildingIcon"
		"xpos"        	"22"
		"ypos"        	"19"
		"zpos"        	"2"
		"wide"        	"56"
		"tall"        	"56"
		"visible"     	"0"
		"enabled"     	"1"
		"scaleImage"  	"1"
		"icon"        	"hud_menu_sentry_build"
		"iconColor"   	"255 255 255 255"	// token: Untinted
	}
	"MetalIcon"
	{
		"ControlName" 	"CIconPanel"
		"fieldName"   	"MetalIcon"
		"xpos"        	"10"
		"ypos"        	"79"
		"zpos"        	"1"
		"wide"        	"10"
		"tall"        	"10"
		"visible"     	"0"
		"enabled"     	"1"
		"scaleImage"  	"1"
		"icon"        	"ico_metal"
		"iconColor"   	"39 38 36 255"	// token: DkCard
	}
	"CostLabel"
	{
		"ControlName"   	"CExLabel"
		"fieldName"     	"CostLabel"
		"font"          	"HudFontSmall"
		"fgcolor"       	"DkPositive"
		"xpos"          	"23"
		"ypos"          	"78"
		"zpos"          	"1"
		"wide"          	"84"
		"tall"          	"13"
		"autoResize"    	"0"
		"pinCorner"     	"0"
		"visible"       	"0"
		"enabled"       	"1"
		"labelText"     	"%metal%"
		"textAlignment" 	"Left"
	}
}
