// ClaudeHUD: migrato ai token (layout originale) - generato da tools/migrate.py
// modalita': dark (DESIGN.md par. 9)
#base "region_base.res"
"Resource/ui/quests/CYOA/regions/region_defense.res"
{
	"Region"
	{
		"ZoomPanel"
		{
			"pending_children"
			{
				"0"
				{
					"child_name" 	"DemoIcon"
				}
				"1"
				{
					"child_name" 	"HeavyIcon"
				}
				"2"
				{
					"child_name" 	"EngineerIcon"
				}
			}
			"DemoIcon"
			{
				"ControlName"          	"ImagePanel"
				"fieldName"            	"DemoIcon"
				"xpos"                 	"185"
				"ypos"                 	"130"
				"zpos"                 	"1"
				"wide"                 	"50"
				"tall"                 	"o1"
				"visible"              	"1"
				"enabled"              	"1"
				"scaleImage"           	"1"
				"image"                	"cyoa/cyoa_icon_demoman"
				"mouseinputenabled"    	"0"
				"keyboardinputenabled" 	"	0"
				"drawcolor"            	"DkChip"
			}
			"HeavyIcon"
			{
				"ControlName"          	"ImagePanel"
				"fieldName"            	"HeavyIcon"
				"xpos"                 	"245"
				"ypos"                 	"130"
				"zpos"                 	"1"
				"wide"                 	"50"
				"tall"                 	"o1"
				"visible"              	"1"
				"enabled"              	"1"
				"scaleImage"           	"1"
				"image"                	"cyoa/cyoa_icon_heavy"
				"mouseinputenabled"    	"0"
				"keyboardinputenabled" 	"	0"
				"drawcolor"            	"DkChip"
			}
			"EngineerIcon"
			{
				"ControlName"          	"ImagePanel"
				"fieldName"            	"EngineerIcon"
				"xpos"                 	"305"
				"ypos"                 	"130"
				"zpos"                 	"1"
				"wide"                 	"50"
				"tall"                 	"o1"
				"visible"              	"1"
				"enabled"              	"1"
				"scaleImage"           	"1"
				"image"                	"cyoa/cyoa_icon_engineer"
				"mouseinputenabled"    	"0"
				"keyboardinputenabled" 	"	0"
				"drawcolor"            	"DkChip"
			}
		}
	}
}
