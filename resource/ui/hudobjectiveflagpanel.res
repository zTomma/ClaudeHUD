// ClaudeHUD: riscritto a mano (fase 4) - CTF: una scheda DkCard 224x44 sul binario inferiore,
// punteggio BLU (SteelLight) e RED (Terracotta) in NumL, valigette di gioco al centro.
// Generato da tools/hand/gen_objectives.py
// ClaudeHUD v2 (taccuino vivace): elementi ClaudeV2* aggiunti da tools/hand/gen_v2.py
"Resource/UI/HudObjectiveFlagPanel.res"
{
	"ObjectiveStatusFlagPanel"
	{
		"ControlName" 	"EditablePanel"
		"fieldName"   	"ObjectiveStatusFlagPanel"
		"xpos"        	"0"
		"ypos"        	"0"
		"zpos"        	"1"
		"wide"        	"f0"
		"tall"        	"480"
		"visible"     	"1"
		"enabled"     	"1"
		"if_hybrid"
		{
			"zpos" 	"-1"
		}
	}
	"LeftSideBG"
	{
		"ControlName" 	"ImagePanel"
		"fieldName"   	"LeftSideBG"
		"xpos"        	"c-140"
		"ypos"        	"r75"
		"zpos"        	"1"
		"wide"        	"0"
		"tall"        	"0"
		"visible"     	"0"
		"enabled"     	"1"
		"image"       	""
		"scaleImage"  	"1"
		"if_hybrid"
		{
			"visible" 	"0"
		}
		"if_mvm"
		{
			"visible" 	"0"
		}
		"if_specialdelivery"
		{
			"visible" 	"0"
		}
		"if_no_flags"
		{
			"visible" 	"0"
		}
	}
	"RightSideBG"
	{
		"ControlName" 	"ImagePanel"
		"fieldName"   	"RightSideBG"
		"xpos"        	"c-140"
		"ypos"        	"r75"
		"zpos"        	"1"
		"wide"        	"0"
		"tall"        	"0"
		"visible"     	"0"
		"enabled"     	"1"
		"image"       	""
		"scaleImage"  	"1"
		"if_hybrid"
		{
			"visible" 	"0"
		}
		"if_mvm"
		{
			"visible" 	"0"
		}
		"if_specialdelivery"
		{
			"visible" 	"0"
		}
		"if_no_flags"
		{
			"visible" 	"0"
		}
	}
	"OutlineBG"
	{
		"ControlName" 	"ImagePanel"
		"fieldName"   	"OutlineBG"
		"xpos"        	"c-140"
		"ypos"        	"r75"
		"zpos"        	"2"
		"wide"        	"0"
		"tall"        	"0"
		"visible"     	"0"
		"enabled"     	"1"
		"image"       	""
		"scaleImage"  	"1"
		"if_hybrid"
		{
			"visible" 	"0"
		}
		"if_mvm"
		{
			"visible" 	"0"
		}
		"if_specialdelivery"
		{
			"visible" 	"0"
		}
		"if_no_flags"
		{
			"visible" 	"0"
		}
	}
	"BlueScore"
	{
		"ControlName"   	"CExLabel"
		"fieldName"     	"BlueScore"
		"xpos"          	"c-108"
		"ypos"          	"r56"
		"zpos"          	"8"
		"wide"          	"36"
		"tall"          	"44"
		"visible"       	"1"
		"enabled"       	"1"
		"textAlignment" 	"center"
		"labelText"     	"%bluescore%"
		"font"          	"NumL"
		"fgcolor"       	"DkBluText"
		"if_hybrid"
		{
			"visible" 	"0"
		}
		"if_mvm"
		{
			"visible" 	"0"
		}
		"if_specialdelivery"
		{
			"visible" 	"0"
		}
		"if_no_flags"
		{
			"visible" 	"0"
		}
	}
	"BlueScoreShadow"
	{
		"ControlName"   	"CExLabel"
		"fieldName"     	"BlueScoreShadow"
		"xpos"          	"c-128"
		"ypos"          	"r46"
		"zpos"          	"7"
		"wide"          	"0"
		"tall"          	"0"
		"visible"       	"1"
		"enabled"       	"1"
		"textAlignment" 	"west"
		"labelText"     	"%bluescore%"
		"font"          	"HudFontBig"
		"fgcolor"       	"Clear"
		"if_hybrid"
		{
			"visible" 	"0"
		}
		"if_mvm"
		{
			"visible" 	"0"
		}
		"if_specialdelivery"
		{
			"visible" 	"0"
		}
		"if_no_flags"
		{
			"visible" 	"0"
		}
	}
	"RedScore"
	{
		"ControlName"   	"CExLabel"
		"fieldName"     	"RedScore"
		"xpos"          	"c72"
		"ypos"          	"r56"
		"zpos"          	"8"
		"wide"          	"36"
		"tall"          	"44"
		"visible"       	"1"
		"enabled"       	"1"
		"textAlignment" 	"center"
		"labelText"     	"%redscore%"
		"font"          	"NumL"
		"fgcolor"       	"DkRedText"
		"if_hybrid"
		{
			"visible" 	"0"
		}
		"if_mvm"
		{
			"visible" 	"0"
		}
		"if_specialdelivery"
		{
			"visible" 	"0"
		}
		"if_no_flags"
		{
			"visible" 	"0"
		}
	}
	"RedScoreShadow"
	{
		"ControlName"   	"CExLabel"
		"fieldName"     	"RedScoreShadow"
		"xpos"          	"c59"
		"ypos"          	"r46"
		"zpos"          	"7"
		"wide"          	"0"
		"tall"          	"0"
		"visible"       	"1"
		"enabled"       	"1"
		"textAlignment" 	"east"
		"labelText"     	"%redscore%"
		"font"          	"HudFontBig"
		"fgcolor"       	"Clear"
		"if_hybrid"
		{
			"visible" 	"0"
		}
		"if_mvm"
		{
			"visible" 	"0"
		}
		"if_specialdelivery"
		{
			"visible" 	"0"
		}
		"if_no_flags"
		{
			"visible" 	"0"
		}
	}
	"OutlineImage"
	{
		"ControlName" 	"CTFImagePanel"
		"fieldName"   	"OutlineImage"
		"xpos"        	"c-50"
		"ypos"        	"r127" [$WIN32]
		"ypos"        	"r148" [$X360]
		"zpos"        	"9"
		"wide"        	"100"
		"tall"        	"50"
		"visible"     	"1"
		"enabled"     	"1"
		"image"       	"../hud/objectives_flagpanel_carried_outline"
		"scaleImage"  	"1"
	}
	"CarriedImage"
	{
		"ControlName" 	"ImagePanel"
		"fieldName"   	"CarriedImage"
		"xpos"        	"c-50"
		"ypos"        	"r137" [$WIN32]
		"ypos"        	"r158" [$X360]
		"zpos"        	"10"
		"wide"        	"100"
		"tall"        	"100"
		"visible"     	"0"
		"enabled"     	"1"
		"image"       	"../hud/objectives_flagpanel_carried_red"
		"scaleImage"  	"1"
		"if_hybrid"
		{
			"ypos" 	"r142"
		}
		"if_specialdelivery"
		{
			"visible" 	"r142"
		}
	}
	"PlayingTo"
	{
		"ControlName"   	"CExLabel"
		"fieldName"     	"PlayingTo"
		"xpos"          	"c-70"
		"ypos"          	"r72"
		"zpos"          	"4"
		"wide"          	"140"
		"tall"          	"12"
		"visible"       	"1"
		"enabled"       	"1"
		"labelText"     	"#TF_PlayingTo"
		"textAlignment" 	"center"
		"dulltext"      	"0"
		"brighttext"    	"0"
		"font"          	"TypeLabel"
		"fgcolor"       	"DkTextMuted"
		"if_hybrid"
		{
			"visible" 	"0"
		}
		"if_mvm"
		{
			"visible" 	"0"
		}
		"if_specialdelivery"
		{
			"visible" 	"0"
		}
		"if_no_flags"
		{
			"visible" 	"0"
		}
		"allcaps"       	"1"
	}
	"PlayingToBG"
	{
		"ControlName" 	"CTFImagePanel"
		"fieldName"   	"PlayingToBG"
		"xpos"        	"c-75"
		"ypos"        	"r31"
		"zpos"        	"3"
		"wide"        	"0"
		"tall"        	"0"
		"visible"     	"0"
		"enabled"     	"1"
		"image"       	""
		"scaleImage"  	"1"
		"if_hybrid"
		{
			"visible" 	"0"
		}
		"if_mvm"
		{
			"visible" 	"0"
		}
		"if_specialdelivery"
		{
			"visible" 	"0"
		}
		"if_no_flags"
		{
			"visible" 	"0"
		}
	}
	"BlueFlag"
	{
		"ControlName" 	"CTFFlagStatus"
		"fieldName"   	"BlueFlag"
		"xpos"        	"c-135"
		"ypos"        	"r77"
		"zpos"        	"5"
		"wide"        	"160"
		"tall"        	"90"
		"visible"     	"1"
		"enabled"     	"1"
		"if_hybrid"
		{
			"visible" 	"0"
			"ypos"    	"r100"
		}
		"if_hybrid_single"
		{
			"xpos" 	"c-80"
		}
		"if_hybrid_double"
		{
			"xpos" 	"c-115"
		}
		"if_specialdelivery"
		{
			"ypos" 	"r100"
		}
		"if_no_flags"
		{
			"visible" 	"0"
		}
	}
	"RedFlag"
	{
		"ControlName" 	"CTFFlagStatus"
		"fieldName"   	"RedFlag"
		"xpos"        	"c-25"
		"ypos"        	"r77"
		"zpos"        	"5"
		"wide"        	"160"
		"tall"        	"90"
		"visible"     	"1"
		"enabled"     	"1"
		"if_hybrid"
		{
			"visible" 	"0"
			"ypos"    	"r100"
		}
		"if_hybrid_single"
		{
			"xpos" 	"c-80"
		}
		"if_hybrid_double"
		{
			"xpos" 	"c-45"
		}
		"if_specialdelivery"
		{
			"ypos" 	"r100"
		}
		"if_no_flags"
		{
			"visible" 	"0"
		}
	}
	"CaptureFlag"
	{
		"ControlName" 	"CTFArrowPanel"
		"fieldName"   	"CaptureFlag"
		"xpos"        	"c-40"
		"ypos"        	"r95" [$WIN32]
		"ypos"        	"r116" [$X360]
		"zpos"        	"5"
		"wide"        	"80"
		"tall"        	"80"
		"visible"     	"0"
		"enabled"     	"1"
		"if_hybrid"
		{
			"ypos" 	"r100"
		}
		"if_specialdelivery"
		{
			"ypos" 	"r100"
		}
	}
	"PoisonIcon"
	{
		"ControlName" 	"ImagePanel"
		"fieldName"   	"PoisonIcon"
		"xpos"        	"cs-0.5"
		"ypos"        	"r75"
		"zpos"        	"6"
		"wide"        	"40"
		"tall"        	"o1"
		"visible"     	"0"
		"enabled"     	"1"
		"image"       	"marked_for_death"
		"scaleImage"  	"1"
	}
	"PoisonTimeLabel"
	{
		"ControlName"   	"CExLabel"
		"fieldName"     	"PoisonTimeLabel"
		"xpos"          	"cs-0.5"
		"ypos"          	"r65"
		"zpos"          	"6"
		"wide"          	"40"
		"tall"          	"20"
		"visible"       	"0"
		"enabled"       	"1"
		"textAlignment" 	"center"
		"labelText"     	"%redscore%"
		"font"          	"HudFontMediumBold"
		"fgcolor"       	"DkText"
	}
	"SpecCarriedImage"
	{
		"ControlName" 	"ImagePanel"
		"fieldName"   	"SpecCarriedImage"
		"xpos"        	"c-50"
		"ypos"        	"r137" [$WIN32]
		"ypos"        	"r158" [$X360]
		"zpos"        	"10"
		"wide"        	"100"
		"tall"        	"100"
		"visible"     	"0"
		"enabled"     	"1"
		"image"       	"../hud/objectives_flagpanel_carried_red"
		"scaleImage"  	"1"
	}
	"FlagScoreCard"
	{
		"ControlName"         	"EditablePanel"
		"fieldName"           	"FlagScoreCard"
		"xpos"                	"c-112"
		"ypos"                	"r56"
		"zpos"                	"-1"
		"wide"                	"224"
		"tall"                	"44"
		"visible"             	"1"
		"enabled"             	"1"
		"paintbackground"     	"1"
		"paintbackgroundtype" 	"2"
		"bgcolor_override"    	"DkCard"
	}
	"ClaudeV2FlagShadow"
	{
		"ControlName"         	"EditablePanel"
		"fieldName"           	"ClaudeV2FlagShadow"
		"xpos"                	"c-109"
		"ypos"                	"r53"
		"zpos"                	"-2"
		"wide"                	"224"
		"tall"                	"44"
		"visible"             	"1"
		"enabled"             	"1"
		"mouseinputenabled"   	"0"
		"paintbackground"     	"1"
		"paintbackgroundtype" 	"2"
		"bgcolor_override"    	"DkShadow"
	}
}
