// ClaudeHUD: migrato ai token (layout originale) - generato da tools/migrate.py
// modalita': light (DESIGN.md par. 9)
"Resource/UI/NavigationPanelTest.res"
{
	"NavTest"
	{
		"ControlName"                   	"CNavigationPanel"
		"fieldName"                     	"NavTest"
		"xpos"                          	"30"
		"ypos"                          	"30"
		"zpos"                          	"6"
		"wide"                          	"50"
		"tall"                          	"300"
		"autoResize"                    	"0"
		"visible"                       	"1"
		"enabled"                       	"1"
		"auto_scale"                    	"1"
		"auto_layout"                   	"1"
		"selected_button_default"       	"0"
		"auto_layout_horizontal_buffer" 	"1"
		"display_vertically"            	"1"
		"ButtonSettings"
		{
			"wide"                      	"20"
			"tall"                      	"40"
			"autoResize"                	"0"
			"pinCorner"                 	"2"
			"visible"                   	"1"
			"enabled"                   	"1"
			"tabPosition"               	"0"
			"labelText"                 	""
			"textAlignment"             	"south-west"
			"scaleImage"                	"1"
			"fgcolor"                   	"111 109 101 255"	// token: LtTextMuted
			"defaultFgColor_override"   	"LtTextMuted"
			"armedFgColor_override"     	"LtTextMuted"
			"depressedFgColor_override" 	"LtTextMuted"
			"sound_depressed"           	"UI/buttonclick.wav"
			"sound_released"            	"UI/buttonclickrelease.wav"
			"sound_armed"               	"UI/buttonrollover.wav"
			"paintbackground"           	"0"
			"paintborder"               	"0"
			"image_drawcolor"           	"255 255 255 178"	// token: UntintedA70
			"image_armedcolor"          	"255 255 255 255"	// token: Untinted
			"image_selectedcolor"       	"255 255 255 255"	// token: Untinted
			"stayselectedonclick"       	"1"
			"keyboardinputenabled"      	"0"
			"SubImage"
			{
				"ControlName" 	"ImagePanel"
				"fieldName"   	"SubImage"
				"xpos"        	"0"
				"ypos"        	"0"
				"zpos"        	"7"
				"wide"        	"100"
				"tall"        	"200"
				"visible"     	"1"
				"enabled"     	"1"
				"scaleImage"  	"1"
			}
		}
		"Buttons"
		{
			"random"
			{
				"image_default"  	"class_sel_sm_random_inactive"
				"image_armed"    	"class_sel_sm_random_inactive"
				"image_selected" 	"class_sel_sm_random_blu"
				"SubImage"
				{
					"image" 	"class_sel_sm_random_inactive"
				}
			}
			"scout"
			{
				"image_default"  	"class_sel_sm_scout_inactive"
				"image_armed"    	"class_sel_sm_scout_inactive"
				"image_selected" 	"class_sel_sm_scout_blu"
				"SubImage"
				{
					"image" 	"class_sel_sm_scout_inactive"
				}
			}
			"soldier"
			{
				"image_default"  	"class_sel_sm_soldier_inactive"
				"image_armed"    	"class_sel_sm_soldier_inactive"
				"image_selected" 	"class_sel_sm_soldier_blu"
				"SubImage"
				{
					"image" 	"class_sel_sm_soldier_inactive"
				}
			}
			"pyro"
			{
				"image_default"  	"class_sel_sm_pyro_inactive"
				"image_armed"    	"class_sel_sm_pyro_inactive"
				"image_selected" 	"class_sel_sm_pyro_blu"
				"SubImage"
				{
					"image" 	"class_sel_sm_pyro_inactive"
				}
			}
			"demoman"
			{
				"image_default"  	"class_sel_sm_demo_inactive"
				"image_armed"    	"class_sel_sm_demo_inactive"
				"image_selected" 	"class_sel_sm_demo_blu"
				"SubImage"
				{
					"image" 	"class_sel_sm_demo_inactive"
				}
			}
			"heavyweapons"
			{
				"image_default"  	"class_sel_sm_heavy_inactive"
				"image_armed"    	"class_sel_sm_heavy_inactive"
				"image_selected" 	"class_sel_sm_heavy_blu"
				"SubImage"
				{
					"image" 	"class_sel_sm_heavy_inactive"
				}
			}
			"engineer"
			{
				"image_default"  	"class_sel_sm_engineer_inactive"
				"image_armed"    	"class_sel_sm_engineer_inactive"
				"image_selected" 	"class_sel_sm_engineer_blu"
				"SubImage"
				{
					"image" 	"class_sel_sm_engineer_inactive"
				}
			}
			"medic"
			{
				"image_default"  	"class_sel_sm_medic_inactive"
				"image_armed"    	"class_sel_sm_medic_inactive"
				"image_selected" 	"class_sel_sm_medic_blu"
				"SubImage"
				{
					"image" 	"class_sel_sm_medic_inactive"
				}
			}
			"sniper"
			{
				"image_default"  	"class_sel_sm_sniper_inactive"
				"image_armed"    	"class_sel_sm_sniper_inactive"
				"image_selected" 	"class_sel_sm_sniper_blu"
				"SubImage"
				{
					"image" 	"class_sel_sm_sniper_inactive"
				}
			}
			"spy"
			{
				"image_default"  	"class_sel_sm_spy_inactive"
				"image_armed"    	"class_sel_sm_spy_inactive"
				"image_selected" 	"class_sel_sm_spy_blu"
				"SubImage"
				{
					"image" 	"class_sel_sm_spy_inactive"
				}
			}
		}
	}
}
