// ClaudeHUD: migrato ai token (layout originale) - generato da tools/migrate.py
// modalita': light (DESIGN.md par. 9)
"Resource/UI/PreviewPanel.res"
{
	"PreviewPanel"
	{
		"ControlName"  	"EditablePanel"
		"fieldName"    	"PreviewPanel"
		"wide"         	"160"
		"zpos"         	"100"
		"autoResize"   	"0"
		"pinCorner"    	"0"
		"visible"      	"0"
		"enabled"      	"1"
		"border"       	"ReplayBalloonBorder"
		"proportional" 	"0"
	}
	"Screenshot"
	{
		"ControlName" 	"ImagePanel"
		"fieldName"   	"Screenshot"
		"zpos"        	"0"
		"autoResize"  	"0"
		"pinCorner"   	"0"
		"enabled"     	"1"
	}
	"InfoPanel"
	{
		"ControlName" 	"EditablePanel"
		"fieldName"   	"InfoPanel"
		"xpos"        	"0"
		"ypos"        	"0"
		"wide"        	"160"
		"tall"        	"75"
		"NoScreenshotLabel"
		{
			"ControlName"      	"CExLabel"
			"FieldName"        	"NoScreenshotLabel"
			"Font"             	"TypeHeading"
			"visible"          	"0"
			"xpos"             	"0"
			"ypos"             	"0"
			"wide"             	"160"
			"tall"             	"15"
			"TextAlignment"    	"center"
			"fgcolor_override" 	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
		}
		"MapLabel"
		{
			"ControlName"      	"CExLabel"
			"FieldName"        	"MapLabel"
			"Font"             	"ReplayMediumSmall"
			"TextAlignment"    	"west"
			"xpos"             	"0"
			"ypos"             	"15"
			"wide"             	"160"
			"tall"             	"10"
			"fgcolor_override" 	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
		}
		"DateTimeLabel"
		{
			"ControlName"      	"CExLabel"
			"FieldName"        	"DateTimeLabel"
			"Font"             	"ReplayBrowserSmallest"
			"TextAlignment"    	"west"
			"fgcolor_override" 	"LtTextMuted"
			"xpos"             	"0"
			"ypos"             	"27"
			"wide"             	"160"
			"tall"             	"15"
		}
		"Label0_0"
		{
			"ControlName"      	"CExLabel"
			"FieldName"        	"Label0_0"
			"Font"             	"DefaultVerySmall"
			"TextAlignment"    	"west"
			"fgcolor_override" 	"LtText"
			"xpos"             	"0"
			"ypos"             	"45"
			"wide"             	"60"
			"tall"             	"10"
			"labelText"        	"#Replay_PlayedAs"
		}
		"Label0_1"
		{
			"ControlName"      	"CExLabel"
			"FieldName"        	"Label0_1"
			"Font"             	"DefaultVerySmall"
			"TextAlignment"    	"west"
			"fgcolor_override" 	"LtText"
			"xpos"             	"60"
			"ypos"             	"45"
			"wide"             	"160"
			"tall"             	"10"
		}
		"Label1_0"
		{
			"ControlName"      	"CExLabel"
			"FieldName"        	"Label1_0"
			"Font"             	"DefaultVerySmall"
			"TextAlignment"    	"west"
			"fgcolor_override" 	"LtText"
			"xpos"             	"0"
			"ypos"             	"55"
			"wide"             	"60"
			"tall"             	"10"
			"labelText"        	"#Replay_KilledBy"
		}
		"Label1_1"
		{
			"ControlName"      	"CExLabel"
			"FieldName"        	"Label1_1"
			"Font"             	"DefaultVerySmall"
			"TextAlignment"    	"west"
			"fgcolor_override" 	"LtText"
			"xpos"             	"60"
			"ypos"             	"55"
			"wide"             	"160"
			"tall"             	"10"
		}
		"Label2_0"
		{
			"ControlName"      	"CExLabel"
			"FieldName"        	"Label2_0"
			"Font"             	"DefaultVerySmall"
			"TextAlignment"    	"west"
			"fgcolor_override" 	"LtText"
			"xpos"             	"0"
			"ypos"             	"65"
			"wide"             	"60"
			"tall"             	"10"
			"labelText"        	"#Replay_LifeLength"
		}
		"Label2_1"
		{
			"ControlName"      	"CExLabel"
			"FieldName"        	"Label2_1"
			"Font"             	"DefaultVerySmall"
			"TextAlignment"    	"west"
			"fgcolor_override" 	"LtText"
			"xpos"             	"60"
			"ypos"             	"65"
			"wide"             	"160"
			"tall"             	"10"
		}
	}
	"ClassImage"
	{
		"ControlName" 	"Panel"
		"FieldName"   	"ClassImage"
		"zpos"        	"102"
	}
}
