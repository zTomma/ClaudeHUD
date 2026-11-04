// ClaudeHUD: migrato ai token (layout originale) - generato da tools/migrate.py
// modalita': light (DESIGN.md par. 9)
"AchievementGroup.res"
{
	"AchievementDialogGroupPanel"
	{
		"ControlName"        	"CAchievementDialogGroupPanel"
		"fieldName"          	"AchievementDialogGroupPanel"
		"xpos"               	"50"
		"ypos"               	"0"
		"wide"               	"260"
		"tall"               	"64"
		"autoResize"         	"0"
		"visible"            	"1"
		"enabled"            	"1"
		"tabPosition"        	"0"
		"settitlebarvisible" 	"0"
		"pinCorner"          	"0"
	}
	"GroupIcon"
	{
		"ControlName" 	"ImagePanel"
		"fieldName"   	"GroupIcon"
		"xpos"        	"0"
		"ypos"        	"0"
		"wide"        	"256"
		"tall"        	"64"
		"visible"     	"1"
		"scaleImage"  	"0"
	}
	"GroupName"
	{
		"ControlName"      	"label"
		"fieldName"        	"GroupName"
		"labeltext"        	""
		"xpos"             	"10"
		"ypos"             	"10"
		"wide"             	"256"
		"tall"             	"20"
		"font"             	"AchievementItemTitle"
		"textAlignment"    	"west"
		"fgcolor_override" 	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"GroupPercentageBarBackground"
	{
		"ControlName" 	"ImagePanel"
		"fieldName"   	"GroupPercentageBarBackground"
		"xpos"        	"20"
		"ypos"        	"40"
		"zpos"        	"2"
		"wide"        	"170"
		"tall"        	"12"
		"fillcolor"   	"255 255 255 255"	// token: LtCard
		"visible"     	"1"
		"enabled"     	"1"
	}
	"GroupPercentageBar"
	{
		"ControlName" 	"ImagePanel"
		"fieldName"   	"GroupPercentageBar"
		"xpos"        	"20"
		"ypos"        	"40"
		"zpos"        	"3"
		"wide"        	"0"
		"tall"        	"12"
		"zpos"        	"0"
		"visible"     	"0"
		"enabled"     	"1"
	}
	"GroupPercentageText"
	{
		"ControlName"      	"Label"
		"fieldName"        	"GroupPercentageText"
		"xpos"             	"200"
		"ypos"             	"40"
		"wide"             	"50"
		"tall"             	"12"
		"autoResize"       	"0"
		"pinCorner"        	"0"
		"visible"          	"1"
		"enabled"          	"1"
		"tabPosition"      	"0"
		"labelText"        	""
		"textAlignment"    	"west"
		"dulltext"         	"0"
		"brighttext"       	"0"
		"wrap"             	"0"
		"font"             	"AchievementItemDescription"
		"fgcolor_override" 	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
}
