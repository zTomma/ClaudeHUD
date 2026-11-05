// ClaudeHUD: migrato ai token (layout originale) - generato da tools/migrate.py
// modalita': dark (DESIGN.md par. 9)
"Resource/UI/HudAchievementFloatingNumber.res"
{
	"FloatingAchievementNumber"
	{
		"ControlName" 	"EditablePanel"
		"fieldName"   	"FloatingAchievementNumber"
		"xpos"        	"0"
		"ypos"        	"0"
		"zpos"        	"4"
		"wide"        	"128"
		"tall"        	"32"
		"visible"     	"1"
		"enabled"     	"1"
	}
	"FloatingNumberLabel"
	{
		"ControlName"   	"Label"
		"fieldName"     	"FloatingNumberLabel"
		"xpos"          	"0"
		"ypos"          	"0"
		"zpos"          	"4"
		"wide"          	"128"
		"tall"          	"32"
		"visible"       	"1"
		"enabled"       	"1"
		"fgcolor"       	"250 249 245 255"	// token: DkText
		"font"          	"ScoreboardMediumSmall"	// AchievementTracker_Name
		"textAlignment" 	"north-west"
	}
}
