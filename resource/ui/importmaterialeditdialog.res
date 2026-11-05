// ClaudeHUD: migrato ai token (layout originale) - generato da tools/migrate.py
// modalita': light (DESIGN.md par. 9)
"ImportMaterialEditDialog.res"
{
	"ImportMaterialEditDialog"
	{
		"fieldName"        	"ImportMaterialEditDialog"
		"visible"          	"1"
		"enabled"          	"1"
		"xpos"             	"0"
		"ypos"             	"0"
		"wide"             	"f0"
		"tall"             	"f0"
		"border"           	"GrayDialogBorder"
		"bgcolor_override" 	"LtCard"	// ClaudeHUD: riempimento al posto del bordo texture
	}
	"Background"
	{
		"ControlName"      	"EditablePanel"
		"fieldName"        	"Background"
		"xpos"             	"0"
		"ypos"             	"0"
		"zpos"             	"-100"
		"wide"             	"f0"
		"tall"             	"f0"
		"pinCorner"        	"0"
		"visible"          	"1"
		"enabled"          	"1"
		"tabPosition"      	"0"
		"bgcolor_override" 	"LtCardAlt"
	}
	"RedBG"
	{
		"ControlName" 	"ImagePanel"
		"fieldName"   	"RedBG"
		"xpos"        	"c-280"
		"ypos"        	"c-290"
		"zpos"        	"-100"
		"wide"        	"560"
		"tall"        	"580"
		"visible"     	"0"
		"enabled"     	"0"
		"image"       	"import_tool_bg_folder_red"
		"scaleImage"  	"1"
	}
	"BlueBG"
	{
		"ControlName" 	"ImagePanel"
		"fieldName"   	"BlueBG"
		"xpos"        	"c-280"
		"ypos"        	"c-290"
		"zpos"        	"-100"
		"wide"        	"560"
		"tall"        	"580"
		"visible"     	"0"
		"enabled"     	"0"
		"image"       	"import_tool_bg_folder_blue"
		"scaleImage"  	"1"
	}
	"RedTeamButton"
	{
		"ControlName"               	"Button"
		"fieldName"                 	"RedTeamButton"
		"xpos"                      	"c-265"
		"ypos"                      	"c-218"
		"wide"                      	"55"
		"tall"                      	"25"
		"autoResize"                	"0"
		"pinCorner"                 	"0"
		"visible"                   	"0"
		"enabled"                   	"0"
		"tabPosition"               	"0"
		"labelText"                 	""
		"textAlignment"             	"center"
		"dulltext"                  	"0"
		"brighttext"                	"0"
		"wrap"                      	"0"
		"Command"                   	"EditSkin0"
		"Default"                   	"0"
		"font"                      	"HudFontSmallBold"
		"defaultBgColor_override"   	"Clear"
		"armedBgColor_override"     	"Clear"
		"defaultFgColor_override"   	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
		"armedFgColor_override"     	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"depressedFgColor_override" 	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"BlueTeamButton"
	{
		"ControlName"               	"Button"
		"fieldName"                 	"BlueTeamButton"
		"xpos"                      	"c-205"
		"ypos"                      	"c-218"
		"wide"                      	"55"
		"tall"                      	"25"
		"autoResize"                	"0"
		"pinCorner"                 	"0"
		"visible"                   	"0"
		"enabled"                   	"0"
		"tabPosition"               	"0"
		"labelText"                 	""
		"textAlignment"             	"center"
		"dulltext"                  	"0"
		"brighttext"                	"0"
		"wrap"                      	"0"
		"Command"                   	"EditSkin1"
		"Default"                   	"0"
		"font"                      	"HudFontSmallBold"
		"defaultBgColor_override"   	"Clear"
		"armedBgColor_override"     	"Clear"
		"defaultFgColor_override"   	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
		"armedFgColor_override"     	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"depressedFgColor_override" 	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"TitleLabel"
	{
		"ControlName"      	"CExLabel"
		"fieldName"        	"TitleLabel"
		"font"             	"TypeHeading"
		"textAlignment"    	"east"
		"labelText"        	""
		"xpos"             	"c-100"
		"ypos"             	"10"
		"zpos"             	"0"
		"wide"             	"200"
		"tall"             	"25"
		"centerwrap"       	"1"
		"fgcolor_override" 	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"BaseTextureBrowse"
	{
		"ControlName"               	"CExImageButton"
		"fieldName"                 	"BaseTextureBrowse"
		"xpos"                      	"c-80"
		"ypos"                      	"60"
		"zpos"                      	"1"
		"wide"                      	"19"
		"tall"                      	"15"
		"autoResize"                	"0"
		"textinsetx"                	"15"
		"use_proportional_insets"   	"1"
		"font"                      	"HudFontSmallBold"
		"textAlignment"             	"west"
		"labelText"                 	""
		"command"                   	"BrowseMaterial"
		"image_drawcolor"           	"20 20 19 255"	// token: LtText
		"image_disabledcolor"       	"20 20 19 255"	// token: LtText
		"SubImage"
		{
			"ControlName" 	"ImagePanel"
			"fieldName"   	"SubImage"
			"xpos"        	"3"
			"ypos"        	"1"
			"zpos"        	"1"
			"wide"        	"13"
			"tall"        	"13"
			"scaleImage"  	"1"
			"image"       	"glyph_workshop_view"
		}
		"defaultFgColor_override"   	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
		"armedFgColor_override"     	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"depressedFgColor_override" 	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"defaultBgColor_override"   	"LtCardAlt"	// ClaudeHUD: colore esplicito in modalita' chiara
		"armedBgColor_override"     	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"depressedBgColor_override" 	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"BaseTextureLabel"
	{
		"ControlName"      	"CExLabel"
		"fieldName"        	"BaseTextureLabel"
		"font"             	"ImportToolSmallestBold"
		"textAlignment"    	"east"
		"labelText"        	"Base Texture"
		"xpos"             	"c-80"
		"ypos"             	"60"
		"zpos"             	"0"
		"wide"             	"80"
		"tall"             	"15"
		"fgcolor_override" 	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"BaseTextureFileLabel"
	{
		"ControlName"      	"Label"
		"fieldName"        	"BaseTextureFileLabel"
		"xpos"             	"c+5"
		"ypos"             	"60"
		"wide"             	"190"
		"tall"             	"15"
		"autoResize"       	"0"
		"pinCorner"        	"0"
		"labelText"        	"#TF_PublishFile_NoFileSelected"
		"font"             	"ImportToolSmallest"
		"fillcolor"        	"217 119 87 255"	// token: LtAccent
		"textAlignment"    	"west"
		"fgcolor_override" 	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"NormalTextureBrowse"
	{
		"ControlName"               	"CExImageButton"
		"fieldName"                 	"NormalTextureBrowse"
		"xpos"                      	"c-105"
		"ypos"                      	"77"
		"zpos"                      	"1"
		"wide"                      	"19"
		"tall"                      	"15"
		"autoResize"                	"0"
		"textinsetx"                	"15"
		"use_proportional_insets"   	"1"
		"font"                      	"HudFontSmallBold"
		"textAlignment"             	"west"
		"labelText"                 	""
		"command"                   	"BrowseNormalTexture"
		"image_drawcolor"           	"20 20 19 255"	// token: LtText
		"image_disabledcolor"       	"20 20 19 255"	// token: LtText
		"SubImage"
		{
			"ControlName" 	"ImagePanel"
			"fieldName"   	"SubImage"
			"xpos"        	"3"
			"ypos"        	"1"
			"zpos"        	"1"
			"wide"        	"13"
			"tall"        	"13"
			"scaleImage"  	"1"
			"image"       	"glyph_workshop_view"
		}
		"defaultFgColor_override"   	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
		"armedFgColor_override"     	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"depressedFgColor_override" 	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"defaultBgColor_override"   	"LtCardAlt"	// ClaudeHUD: colore esplicito in modalita' chiara
		"armedBgColor_override"     	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"depressedBgColor_override" 	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"NormalTextureClear"
	{
		"ControlName"               	"CExImageButton"
		"fieldName"                 	"NormalTextureClear"
		"xpos"                      	"c-84"
		"ypos"                      	"77"
		"wide"                      	"15"
		"tall"                      	"15"
		"autoResize"                	"0"
		"pinCorner"                 	"3"
		"textinsetx"                	"15"
		"use_proportional_insets"   	"1"
		"font"                      	"HudFontSmallBold"
		"textAlignment"             	"west"
		"labelText"                 	""
		"command"                   	"ClearNormalTexture"
		"image_drawcolor"           	"20 20 19 255"	// token: LtText
		"image_disabledcolor"       	"20 20 19 255"	// token: LtText
		"SubImage"
		{
			"ControlName" 	"ImagePanel"
			"fieldName"   	"SubImage"
			"xpos"        	"1"
			"ypos"        	"1"
			"zpos"        	"1"
			"wide"        	"13"
			"tall"        	"13"
			"scaleImage"  	"1"
			"image"       	"glyph_close_X"
		}
		"defaultFgColor_override"   	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
		"armedFgColor_override"     	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"depressedFgColor_override" 	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"defaultBgColor_override"   	"LtCardAlt"	// ClaudeHUD: colore esplicito in modalita' chiara
		"armedBgColor_override"     	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"depressedBgColor_override" 	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"NormalTextureLabel"
	{
		"ControlName"      	"CExLabel"
		"fieldName"        	"NormalTextureLabel"
		"font"             	"ImportToolSmallestBold"
		"textAlignment"    	"east"
		"labelText"        	"Shared Normal"
		"xpos"             	"c-70"
		"ypos"             	"77"
		"zpos"             	"0"
		"wide"             	"70"
		"tall"             	"15"
		"fgcolor_override" 	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"NormalTextureFileLabel"
	{
		"ControlName"      	"Label"
		"fieldName"        	"NormalTextureFileLabel"
		"xpos"             	"c+5"
		"ypos"             	"77"
		"wide"             	"190"
		"tall"             	"15"
		"autoResize"       	"0"
		"pinCorner"        	"0"
		"labelText"        	"#TF_PublishFile_Optional"
		"font"             	"ImportToolSmallest"
		"fillcolor"        	"217 119 87 255"	// token: LtAccent
		"textAlignment"    	"west"
		"fgcolor_override" 	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"LightwarpLabel"
	{
		"ControlName"      	"CExLabel"
		"fieldName"        	"LightwarpLabel"
		"font"             	"ImportToolSmallestBold"
		"textAlignment"    	"east"
		"labelText"        	"Lightwarp"
		"xpos"             	"c-80"
		"ypos"             	"90"
		"zpos"             	"0"
		"wide"             	"80"
		"tall"             	"15"
		"fgcolor_override" 	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"LightwarpComboBox"
	{
		"ControlName" 	"ComboBox"
		"fieldName"   	"LightwarpComboBox"
		"Font"        	"ImportToolSmallest"
		"xpos"        	"c+5"
		"ypos"        	"90"
		"wide"        	"175"
		"tall"        	"12"
		"autoResize"  	"0"
		"pinCorner"   	"0"
		"editable"    	"0"
		"visible"     	"1"
	}
	"BaseMapAlphaPhongMaskLabel"
	{
		"ControlName"      	"CExLabel"
		"fieldName"        	"BaseMapAlphaPhongMaskLabel"
		"font"             	"ImportToolSmallestBold"
		"textAlignment"    	"east"
		"labelText"        	"Base Map Alpha Phong Mask"
		"xpos"             	"c-125"
		"ypos"             	"105"
		"zpos"             	"0"
		"wide"             	"125"
		"tall"             	"15"
		"fgcolor_override" 	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"BaseMapAlphaPhongMaskCheckButton"
	{
		"ControlName"               	"CheckButton"
		"fieldName"                 	"BaseMapAlphaPhongMaskCheckButton"
		"labelText"                 	""
		"Font"                      	"ImportToolSmallestBold"
		"textAlignment"             	"west"
		"xpos"                      	"c+1"
		"ypos"                      	"103"
		"wide"                      	"30"
		"tall"                      	"20"
		"autoResize"                	"0"
		"pinCorner"                 	"0"
		"visible"                   	"1"
		"enabled"                   	"1"
		"dulltext"                  	"0"
		"brighttext"                	"0"
		"command"                   	"UpdateBaseMapAlphaPhongMask"
		"border"                    	"SteamWorkshopBorder"
		"fgcolor_override"          	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
		"defaultBgColor_override"   	"LtCardAlt"	// ClaudeHUD: riempimento al posto del bordo texture
		"armedBgColor_override"     	"LtButtonHover"	// ClaudeHUD: riempimento al posto del bordo texture
		"depressedBgColor_override" 	"LtButtonHover"	// ClaudeHUD: riempimento al posto del bordo texture
		"defaultFgColor_override"   	"LtText"	// ClaudeHUD: riempimento al posto del bordo texture
		"armedFgColor_override"     	"LtOnButtonHover"	// ClaudeHUD: riempimento al posto del bordo texture
		"depressedFgColor_override" 	"LtOnButtonHover"	// ClaudeHUD: riempimento al posto del bordo texture
	}
	"PhongExponentTextureBrowse"
	{
		"ControlName"               	"CExImageButton"
		"fieldName"                 	"PhongExponentTextureBrowse"
		"xpos"                      	"c-196"
		"ypos"                      	"125"
		"zpos"                      	"1"
		"wide"                      	"19"
		"tall"                      	"15"
		"autoResize"                	"0"
		"textinsetx"                	"15"
		"use_proportional_insets"   	"1"
		"font"                      	"HudFontSmallBold"
		"textAlignment"             	"west"
		"labelText"                 	""
		"command"                   	"BrowsePhongExponentTexture"
		"image_drawcolor"           	"20 20 19 255"	// token: LtText
		"image_disabledcolor"       	"20 20 19 255"	// token: LtText
		"SubImage"
		{
			"ControlName" 	"ImagePanel"
			"fieldName"   	"SubImage"
			"xpos"        	"3"
			"ypos"        	"1"
			"zpos"        	"1"
			"wide"        	"13"
			"tall"        	"13"
			"scaleImage"  	"1"
			"image"       	"glyph_workshop_view"
		}
		"defaultFgColor_override"   	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
		"armedFgColor_override"     	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"depressedFgColor_override" 	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"defaultBgColor_override"   	"LtCardAlt"	// ClaudeHUD: colore esplicito in modalita' chiara
		"armedBgColor_override"     	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"depressedBgColor_override" 	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"PhongExponentTextureClear"
	{
		"ControlName"               	"CExImageButton"
		"fieldName"                 	"PhongExponentTextureClear"
		"xpos"                      	"c-175"
		"ypos"                      	"125"
		"wide"                      	"15"
		"tall"                      	"15"
		"autoResize"                	"0"
		"pinCorner"                 	"3"
		"textinsetx"                	"15"
		"use_proportional_insets"   	"1"
		"font"                      	"HudFontSmallBold"
		"textAlignment"             	"west"
		"labelText"                 	""
		"command"                   	"ClearPhongExponentTexture"
		"image_drawcolor"           	"20 20 19 255"	// token: LtText
		"image_disabledcolor"       	"20 20 19 255"	// token: LtText
		"SubImage"
		{
			"ControlName" 	"ImagePanel"
			"fieldName"   	"SubImage"
			"xpos"        	"1"
			"ypos"        	"1"
			"zpos"        	"1"
			"wide"        	"13"
			"tall"        	"13"
			"scaleImage"  	"1"
			"image"       	"glyph_close_X"
		}
		"defaultFgColor_override"   	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
		"armedFgColor_override"     	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"depressedFgColor_override" 	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"defaultBgColor_override"   	"LtCardAlt"	// ClaudeHUD: colore esplicito in modalita' chiara
		"armedBgColor_override"     	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"depressedBgColor_override" 	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"PhongExponentTextureLabel"
	{
		"ControlName"      	"CExLabel"
		"fieldName"        	"PhongExponentTextureLabel"
		"font"             	"ImportToolSmallestBold"
		"textAlignment"    	"east"
		"labelText"        	"Shared Phong Exponent / Rim Mask"
		"xpos"             	"c-170"
		"ypos"             	"125"
		"zpos"             	"0"
		"wide"             	"170"
		"tall"             	"15"
		"fgcolor_override" 	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"PhongExponentTextureFileLabel"
	{
		"ControlName"      	"Label"
		"fieldName"        	"PhongExponentTextureFileLabel"
		"xpos"             	"c+5"
		"ypos"             	"125"
		"wide"             	"190"
		"tall"             	"15"
		"autoResize"       	"0"
		"pinCorner"        	"0"
		"labelText"        	"#TF_PublishFile_Optional"
		"font"             	"ImportToolSmallest"
		"fillcolor"        	"217 119 87 255"	// token: LtAccent
		"textAlignment"    	"west"
		"fgcolor_override" 	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"PhongExponentLabel"
	{
		"ControlName"      	"CExLabel"
		"fieldName"        	"PhongExponentLabel"
		"font"             	"ImportToolSmallestBold"
		"textAlignment"    	"east"
		"labelText"        	"Phong Exponent"
		"xpos"             	"c-100"
		"ypos"             	"145"
		"zpos"             	"0"
		"wide"             	"100"
		"tall"             	"15"
		"fgcolor_override" 	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"PhongExponentTextEntry"
	{
		"ControlName"         	"TextEntry"
		"fieldName"           	"PhongExponentTextEntry"
		"xpos"                	"c+5"
		"ypos"                	"145"
		"wide"                	"35"
		"tall"                	"12"
		"autoResize"          	"0"
		"pinCorner"           	"0"
		"visible"             	"1"
		"enabled"             	"1"
		"tabPosition"         	"1"
		"textHidden"          	"0"
		"editable"            	"1"
		"maxchars"            	"128"
		"NumericInputOnly"    	"1"
		"unicode"             	"1"
		"fgcolor_override"    	"LtText"
		"bgcolor_override"    	"LtButtonHover"
		"paintbackgroundtype" 	"2"
		"font"                	"ImportToolSmallest"
	}
	"PhongBoostLabel"
	{
		"ControlName"      	"CExLabel"
		"fieldName"        	"PhongBoostLabel"
		"font"             	"ImportToolSmallestBold"
		"textAlignment"    	"east"
		"labelText"        	"Phong Boost"
		"xpos"             	"c-100"
		"ypos"             	"160"
		"zpos"             	"0"
		"wide"             	"100"
		"tall"             	"15"
		"fgcolor_override" 	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"PhongBoostTextEntry"
	{
		"ControlName"         	"TextEntry"
		"fieldName"           	"PhongBoostTextEntry"
		"xpos"                	"c+5"
		"ypos"                	"160"
		"wide"                	"35"
		"tall"                	"12"
		"autoResize"          	"0"
		"pinCorner"           	"0"
		"visible"             	"1"
		"enabled"             	"1"
		"tabPosition"         	"1"
		"textHidden"          	"0"
		"editable"            	"1"
		"maxchars"            	"128"
		"NumericInputOnly"    	"1"
		"unicode"             	"1"
		"fgcolor_override"    	"LtText"
		"bgcolor_override"    	"LtButtonHover"
		"paintbackgroundtype" 	"2"
		"font"                	"ImportToolSmallest"
	}
	"RimLightExponentLabel"
	{
		"ControlName"      	"CExLabel"
		"fieldName"        	"RimLightExponentLabel"
		"font"             	"ImportToolSmallestBold"
		"textAlignment"    	"east"
		"labelText"        	"Rim Light Exponent"
		"xpos"             	"c-100"
		"ypos"             	"175"
		"zpos"             	"0"
		"wide"             	"100"
		"tall"             	"15"
		"fgcolor_override" 	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"RimLightExponentTextEntry"
	{
		"ControlName"         	"TextEntry"
		"fieldName"           	"RimLightExponentTextEntry"
		"xpos"                	"c+5"
		"ypos"                	"175"
		"wide"                	"35"
		"tall"                	"12"
		"autoResize"          	"0"
		"pinCorner"           	"0"
		"visible"             	"1"
		"enabled"             	"1"
		"tabPosition"         	"1"
		"textHidden"          	"0"
		"editable"            	"1"
		"maxchars"            	"128"
		"NumericInputOnly"    	"1"
		"unicode"             	"1"
		"fgcolor_override"    	"LtText"
		"bgcolor_override"    	"LtButtonHover"
		"paintbackgroundtype" 	"2"
		"font"                	"ImportToolSmallest"
	}
	"RimLightBoostLabel"
	{
		"ControlName"      	"CExLabel"
		"fieldName"        	"RimLightBoostLabel"
		"font"             	"ImportToolSmallestBold"
		"textAlignment"    	"east"
		"labelText"        	"Rim Light Boost"
		"xpos"             	"c-100"
		"ypos"             	"190"
		"zpos"             	"0"
		"wide"             	"100"
		"tall"             	"15"
		"fgcolor_override" 	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"RimLightBoostTextEntry"
	{
		"ControlName"         	"TextEntry"
		"fieldName"           	"RimLightBoostTextEntry"
		"xpos"                	"c+5"
		"ypos"                	"190"
		"wide"                	"35"
		"tall"                	"12"
		"autoResize"          	"0"
		"pinCorner"           	"0"
		"visible"             	"1"
		"enabled"             	"1"
		"tabPosition"         	"1"
		"textHidden"          	"0"
		"editable"            	"1"
		"maxchars"            	"128"
		"NumericInputOnly"    	"1"
		"unicode"             	"1"
		"fgcolor_override"    	"LtText"
		"bgcolor_override"    	"LtButtonHover"
		"paintbackgroundtype" 	"2"
		"font"                	"ImportToolSmallest"
	}
	"RimMaskLabel"
	{
		"ControlName"      	"CExLabel"
		"fieldName"        	"RimMaskLabel"
		"font"             	"ImportToolSmallestBold"
		"textAlignment"    	"east"
		"labelText"        	"Rim Mask"
		"xpos"             	"c-100"
		"ypos"             	"205"
		"zpos"             	"0"
		"wide"             	"100"
		"tall"             	"15"
		"enabled"          	"0"
		"fgcolor_override" 	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"RimMaskCheckButton"
	{
		"ControlName"               	"CheckButton"
		"fieldName"                 	"RimMaskCheckButton"
		"labelText"                 	""
		"Font"                      	"ImportToolSmallestBold"
		"textAlignment"             	"west"
		"xpos"                      	"c+1"
		"ypos"                      	"203"
		"wide"                      	"30"
		"tall"                      	"20"
		"autoResize"                	"0"
		"pinCorner"                 	"0"
		"visible"                   	"1"
		"enabled"                   	"0"
		"dulltext"                  	"0"
		"brighttext"                	"0"
		"command"                   	"UpdateRimMask"
		"border"                    	"SteamWorkshopBorder"
		"fgcolor_override"          	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
		"defaultBgColor_override"   	"LtCardAlt"	// ClaudeHUD: riempimento al posto del bordo texture
		"armedBgColor_override"     	"LtButtonHover"	// ClaudeHUD: riempimento al posto del bordo texture
		"depressedBgColor_override" 	"LtButtonHover"	// ClaudeHUD: riempimento al posto del bordo texture
		"defaultFgColor_override"   	"LtText"	// ClaudeHUD: riempimento al posto del bordo texture
		"armedFgColor_override"     	"LtOnButtonHover"	// ClaudeHUD: riempimento al posto del bordo texture
		"depressedFgColor_override" 	"LtOnButtonHover"	// ClaudeHUD: riempimento al posto del bordo texture
	}
	"HalfLambertLabel"
	{
		"ControlName"      	"CExLabel"
		"fieldName"        	"HalfLambertLabel"
		"font"             	"ImportToolSmallestBold"
		"textAlignment"    	"east"
		"labelText"        	"Half Lambert"
		"xpos"             	"c-100"
		"ypos"             	"225"
		"zpos"             	"0"
		"wide"             	"100"
		"tall"             	"15"
		"fgcolor_override" 	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"HalfLambertCheckButton"
	{
		"ControlName"               	"CheckButton"
		"fieldName"                 	"HalfLambertCheckButton"
		"labelText"                 	""
		"Font"                      	"ImportToolSmallestBold"
		"textAlignment"             	"west"
		"xpos"                      	"c+1"
		"ypos"                      	"223"
		"wide"                      	"30"
		"tall"                      	"20"
		"autoResize"                	"0"
		"pinCorner"                 	"0"
		"visible"                   	"1"
		"enabled"                   	"1"
		"dulltext"                  	"0"
		"brighttext"                	"0"
		"command"                   	"UpdateHalfLambert"
		"border"                    	"SteamWorkshopBorder"
		"fgcolor_override"          	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
		"defaultBgColor_override"   	"LtCardAlt"	// ClaudeHUD: riempimento al posto del bordo texture
		"armedBgColor_override"     	"LtButtonHover"	// ClaudeHUD: riempimento al posto del bordo texture
		"depressedBgColor_override" 	"LtButtonHover"	// ClaudeHUD: riempimento al posto del bordo texture
		"defaultFgColor_override"   	"LtText"	// ClaudeHUD: riempimento al posto del bordo texture
		"armedFgColor_override"     	"LtOnButtonHover"	// ClaudeHUD: riempimento al posto del bordo texture
		"depressedFgColor_override" 	"LtOnButtonHover"	// ClaudeHUD: riempimento al posto del bordo texture
	}
	"BlendTintByBaseAlphaLabel"
	{
		"ControlName"      	"CExLabel"
		"fieldName"        	"BlendTintByBaseAlphaLabel"
		"font"             	"ImportToolSmallestBold"
		"textAlignment"    	"east"
		"labelText"        	"Blend Tint By Base Alpha"
		"xpos"             	"c-150"
		"ypos"             	"245"
		"zpos"             	"0"
		"wide"             	"150"
		"tall"             	"15"
		"enabled"          	"0"
		"fgcolor_override" 	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"BlendTintByBaseAlphaCheckButton"
	{
		"ControlName"               	"CheckButton"
		"fieldName"                 	"BlendTintByBaseAlphaCheckButton"
		"labelText"                 	""
		"Font"                      	"ImportToolSmallestBold"
		"textAlignment"             	"west"
		"xpos"                      	"c+1"
		"ypos"                      	"243"
		"wide"                      	"30"
		"tall"                      	"20"
		"autoResize"                	"0"
		"pinCorner"                 	"0"
		"visible"                   	"1"
		"enabled"                   	"0"
		"dulltext"                  	"0"
		"brighttext"                	"0"
		"command"                   	"UpdateBlendTintByBaseAlpha"
		"border"                    	"SteamWorkshopBorder"
		"fgcolor_override"          	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
		"defaultBgColor_override"   	"LtCardAlt"	// ClaudeHUD: riempimento al posto del bordo texture
		"armedBgColor_override"     	"LtButtonHover"	// ClaudeHUD: riempimento al posto del bordo texture
		"depressedBgColor_override" 	"LtButtonHover"	// ClaudeHUD: riempimento al posto del bordo texture
		"defaultFgColor_override"   	"LtText"	// ClaudeHUD: riempimento al posto del bordo texture
		"armedFgColor_override"     	"LtOnButtonHover"	// ClaudeHUD: riempimento al posto del bordo texture
		"depressedFgColor_override" 	"LtOnButtonHover"	// ClaudeHUD: riempimento al posto del bordo texture
	}
	"BlendTintColorOverBaseLabel"
	{
		"ControlName"      	"CExLabel"
		"fieldName"        	"BlendTintColorOverBaseLabel"
		"font"             	"ImportToolSmallestBold"
		"textAlignment"    	"east"
		"labelText"        	"Blend Tint Color Over Base"
		"xpos"             	"c-150"
		"ypos"             	"265"
		"zpos"             	"0"
		"wide"             	"150"
		"tall"             	"15"
		"enabled"          	"0"
		"fgcolor_override" 	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"BlendTintColorOverBaseTextEntry"
	{
		"ControlName"         	"TextEntry"
		"fieldName"           	"BlendTintColorOverBaseTextEntry"
		"xpos"                	"c+5"
		"ypos"                	"265"
		"wide"                	"35"
		"tall"                	"12"
		"autoResize"          	"0"
		"pinCorner"           	"0"
		"visible"             	"1"
		"enabled"             	"0"
		"tabPosition"         	"1"
		"textHidden"          	"0"
		"editable"            	"1"
		"maxchars"            	"128"
		"NumericInputOnly"    	"1"
		"unicode"             	"1"
		"fgcolor_override"    	"LtText"
		"bgcolor_override"    	"LtButtonHover"
		"paintbackgroundtype" 	"2"
		"font"                	"ImportToolSmallest"
	}
	"ColorTintBaseLabel"
	{
		"ControlName"      	"CExLabel"
		"fieldName"        	"ColorTintBaseLabel"
		"font"             	"ImportToolSmallestBold"
		"textAlignment"    	"east"
		"labelText"        	"Color Tint Base (RGB)"
		"xpos"             	"c-150"
		"ypos"             	"280"
		"zpos"             	"0"
		"wide"             	"150"
		"tall"             	"15"
		"enabled"          	"0"
		"fgcolor_override" 	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"ColorTintBaseRedTextEntry"
	{
		"ControlName"         	"TextEntry"
		"fieldName"           	"ColorTintBaseRedTextEntry"
		"xpos"                	"c+5"
		"ypos"                	"280"
		"wide"                	"35"
		"tall"                	"12"
		"autoResize"          	"0"
		"pinCorner"           	"0"
		"visible"             	"1"
		"enabled"             	"0"
		"tabPosition"         	"1"
		"textHidden"          	"0"
		"editable"            	"1"
		"maxchars"            	"128"
		"NumericInputOnly"    	"1"
		"unicode"             	"1"
		"fgcolor_override"    	"LtText"
		"bgcolor_override"    	"LtButtonHover"
		"paintbackgroundtype" 	"2"
		"font"                	"ImportToolSmallest"
	}
	"ColorTintBaseGreenTextEntry"
	{
		"ControlName"         	"TextEntry"
		"fieldName"           	"ColorTintBaseGreenTextEntry"
		"xpos"                	"c+45"
		"ypos"                	"280"
		"wide"                	"35"
		"tall"                	"12"
		"autoResize"          	"0"
		"pinCorner"           	"0"
		"visible"             	"1"
		"enabled"             	"0"
		"tabPosition"         	"1"
		"textHidden"          	"0"
		"editable"            	"1"
		"maxchars"            	"128"
		"NumericInputOnly"    	"1"
		"unicode"             	"1"
		"fgcolor_override"    	"LtText"
		"bgcolor_override"    	"LtButtonHover"
		"paintbackgroundtype" 	"2"
		"font"                	"ImportToolSmallest"
	}
	"ColorTintBaseBlueTextEntry"
	{
		"ControlName"         	"TextEntry"
		"fieldName"           	"ColorTintBaseBlueTextEntry"
		"xpos"                	"c+85"
		"ypos"                	"280"
		"wide"                	"35"
		"tall"                	"12"
		"autoResize"          	"0"
		"pinCorner"           	"0"
		"visible"             	"1"
		"enabled"             	"0"
		"tabPosition"         	"1"
		"textHidden"          	"0"
		"editable"            	"1"
		"maxchars"            	"128"
		"NumericInputOnly"    	"1"
		"unicode"             	"1"
		"fgcolor_override"    	"LtText"
		"bgcolor_override"    	"LtButtonHover"
		"paintbackgroundtype" 	"2"
		"font"                	"ImportToolSmallest"
	}
	"AdditiveLabel"
	{
		"ControlName"      	"CExLabel"
		"fieldName"        	"AdditiveLabel"
		"font"             	"ImportToolSmallestBold"
		"textAlignment"    	"east"
		"labelText"        	"Additive"
		"xpos"             	"c-100"
		"ypos"             	"295"
		"zpos"             	"0"
		"wide"             	"100"
		"tall"             	"15"
		"fgcolor_override" 	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"AdditiveCheckButton"
	{
		"ControlName"               	"CheckButton"
		"fieldName"                 	"AdditiveCheckButton"
		"labelText"                 	""
		"Font"                      	"ImportToolSmallestBold"
		"textAlignment"             	"west"
		"xpos"                      	"c+1"
		"ypos"                      	"293"
		"wide"                      	"30"
		"tall"                      	"20"
		"autoResize"                	"0"
		"pinCorner"                 	"0"
		"visible"                   	"1"
		"enabled"                   	"1"
		"dulltext"                  	"0"
		"brighttext"                	"0"
		"command"                   	"UpdateAdditive"
		"border"                    	"SteamWorkshopBorder"
		"fgcolor_override"          	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
		"defaultBgColor_override"   	"LtCardAlt"	// ClaudeHUD: riempimento al posto del bordo texture
		"armedBgColor_override"     	"LtButtonHover"	// ClaudeHUD: riempimento al posto del bordo texture
		"depressedBgColor_override" 	"LtButtonHover"	// ClaudeHUD: riempimento al posto del bordo texture
		"defaultFgColor_override"   	"LtText"	// ClaudeHUD: riempimento al posto del bordo texture
		"armedFgColor_override"     	"LtOnButtonHover"	// ClaudeHUD: riempimento al posto del bordo texture
		"depressedFgColor_override" 	"LtOnButtonHover"	// ClaudeHUD: riempimento al posto del bordo texture
	}
	"TranslucentLabel"
	{
		"ControlName"      	"CExLabel"
		"fieldName"        	"TranslucentLabel"
		"font"             	"ImportToolSmallestBold"
		"textAlignment"    	"east"
		"labelText"        	"Translucent"
		"xpos"             	"c+19"
		"ypos"             	"295"
		"zpos"             	"0"
		"wide"             	"60"
		"tall"             	"15"
		"fgcolor_override" 	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"TranslucentCheckButton"
	{
		"ControlName"               	"CheckButton"
		"fieldName"                 	"TranslucentCheckButton"
		"labelText"                 	""
		"Font"                      	"ImportToolSmallestBold"
		"textAlignment"             	"west"
		"xpos"                      	"c+81"
		"ypos"                      	"293"
		"wide"                      	"30"
		"tall"                      	"20"
		"autoResize"                	"0"
		"pinCorner"                 	"0"
		"visible"                   	"1"
		"enabled"                   	"1"
		"dulltext"                  	"0"
		"brighttext"                	"0"
		"command"                   	"UpdateTranslucent"
		"border"                    	"SteamWorkshopBorder"
		"fgcolor_override"          	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
		"defaultBgColor_override"   	"LtCardAlt"	// ClaudeHUD: riempimento al posto del bordo texture
		"armedBgColor_override"     	"LtButtonHover"	// ClaudeHUD: riempimento al posto del bordo texture
		"depressedBgColor_override" 	"LtButtonHover"	// ClaudeHUD: riempimento al posto del bordo texture
		"defaultFgColor_override"   	"LtText"	// ClaudeHUD: riempimento al posto del bordo texture
		"armedFgColor_override"     	"LtOnButtonHover"	// ClaudeHUD: riempimento al posto del bordo texture
		"depressedFgColor_override" 	"LtOnButtonHover"	// ClaudeHUD: riempimento al posto del bordo texture
	}
	"AlphaTestLabel"
	{
		"ControlName"      	"CExLabel"
		"fieldName"        	"AlphaTestLabel"
		"font"             	"ImportToolSmallestBold"
		"textAlignment"    	"east"
		"labelText"        	"Alpha Test"
		"xpos"             	"c+96"
		"ypos"             	"295"
		"zpos"             	"0"
		"wide"             	"60"
		"tall"             	"15"
		"enabled"          	"0"
		"fgcolor_override" 	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"AlphaTestCheckButton"
	{
		"ControlName"               	"CheckButton"
		"fieldName"                 	"AlphaTestCheckButton"
		"labelText"                 	""
		"Font"                      	"ImportToolSmallestBold"
		"textAlignment"             	"west"
		"xpos"                      	"c+158"
		"ypos"                      	"293"
		"wide"                      	"30"
		"tall"                      	"20"
		"autoResize"                	"0"
		"pinCorner"                 	"0"
		"visible"                   	"1"
		"enabled"                   	"0"
		"dulltext"                  	"0"
		"brighttext"                	"0"
		"command"                   	"UpdateAlphaTest"
		"border"                    	"SteamWorkshopBorder"
		"fgcolor_override"          	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
		"defaultBgColor_override"   	"LtCardAlt"	// ClaudeHUD: riempimento al posto del bordo texture
		"armedBgColor_override"     	"LtButtonHover"	// ClaudeHUD: riempimento al posto del bordo texture
		"depressedBgColor_override" 	"LtButtonHover"	// ClaudeHUD: riempimento al posto del bordo texture
		"defaultFgColor_override"   	"LtText"	// ClaudeHUD: riempimento al posto del bordo texture
		"armedFgColor_override"     	"LtOnButtonHover"	// ClaudeHUD: riempimento al posto del bordo texture
		"depressedFgColor_override" 	"LtOnButtonHover"	// ClaudeHUD: riempimento al posto del bordo texture
	}
	"EnvmapLabel"
	{
		"ControlName"      	"CExLabel"
		"fieldName"        	"EnvmapLabel"
		"font"             	"ImportToolSmallestBold"
		"textAlignment"    	"east"
		"labelText"        	"Cube Map"
		"xpos"             	"c-100"
		"ypos"             	"315"
		"zpos"             	"0"
		"wide"             	"100"
		"tall"             	"15"
		"fgcolor_override" 	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"EnvmapComboBox"
	{
		"ControlName" 	"ComboBox"
		"fieldName"   	"EnvmapComboBox"
		"Font"        	"ImportToolSmallest"
		"xpos"        	"c+5"
		"ypos"        	"315"
		"wide"        	"175"
		"tall"        	"12"
		"autoResize"  	"0"
		"pinCorner"   	"0"
		"editable"    	"0"
		"visible"     	"1"
	}
	"EnvmapAlphaMaskLabel"
	{
		"ControlName"      	"CExLabel"
		"fieldName"        	"EnvmapAlphaMaskLabel"
		"font"             	"ImportToolSmallestBold"
		"textAlignment"    	"east"
		"labelText"        	"Cube Map Alpha Mask"
		"xpos"             	"c-150"
		"ypos"             	"330"
		"zpos"             	"0"
		"wide"             	"150"
		"tall"             	"15"
		"enabled"          	"0"
		"fgcolor_override" 	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"EnvmapAlphaMaskComboBox"
	{
		"ControlName" 	"ComboBox"
		"fieldName"   	"EnvmapAlphaMaskComboBox"
		"Font"        	"ImportToolSmallest"
		"xpos"        	"c+5"
		"ypos"        	"330"
		"wide"        	"175"
		"tall"        	"12"
		"autoResize"  	"0"
		"pinCorner"   	"0"
		"editable"    	"0"
		"visible"     	"1"
		"enabled"     	"0"
	}
	"EnvmapTintLabel"
	{
		"ControlName"      	"CExLabel"
		"fieldName"        	"EnvmapTintLabel"
		"font"             	"ImportToolSmallestBold"
		"textAlignment"    	"east"
		"labelText"        	"Cube Map Tint (RGB)"
		"xpos"             	"c-150"
		"ypos"             	"345"
		"zpos"             	"0"
		"wide"             	"150"
		"tall"             	"15"
		"enabled"          	"0"
		"fgcolor_override" 	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"CubemapTintRedTextEntry"
	{
		"ControlName"         	"TextEntry"
		"fieldName"           	"CubemapTintRedTextEntry"
		"xpos"                	"c+5"
		"ypos"                	"345"
		"wide"                	"35"
		"tall"                	"12"
		"autoResize"          	"0"
		"pinCorner"           	"0"
		"visible"             	"1"
		"enabled"             	"0"
		"tabPosition"         	"1"
		"textHidden"          	"0"
		"editable"            	"1"
		"maxchars"            	"128"
		"NumericInputOnly"    	"1"
		"unicode"             	"1"
		"fgcolor_override"    	"LtText"
		"bgcolor_override"    	"LtButtonHover"
		"paintbackgroundtype" 	"2"
		"font"                	"ImportToolSmallest"
	}
	"CubemapTintGreenTextEntry"
	{
		"ControlName"         	"TextEntry"
		"fieldName"           	"CubemapTintGreenTextEntry"
		"xpos"                	"c+45"
		"ypos"                	"345"
		"wide"                	"35"
		"tall"                	"12"
		"autoResize"          	"0"
		"pinCorner"           	"0"
		"visible"             	"1"
		"enabled"             	"0"
		"tabPosition"         	"1"
		"textHidden"          	"0"
		"editable"            	"1"
		"maxchars"            	"128"
		"NumericInputOnly"    	"1"
		"unicode"             	"1"
		"fgcolor_override"    	"LtText"
		"bgcolor_override"    	"LtButtonHover"
		"paintbackgroundtype" 	"2"
		"font"                	"ImportToolSmallest"
	}
	"CubemapTintBlueTextEntry"
	{
		"ControlName"         	"TextEntry"
		"fieldName"           	"CubemapTintBlueTextEntry"
		"xpos"                	"c+85"
		"ypos"                	"345"
		"wide"                	"35"
		"tall"                	"12"
		"autoResize"          	"0"
		"pinCorner"           	"0"
		"visible"             	"1"
		"enabled"             	"0"
		"tabPosition"         	"1"
		"textHidden"          	"0"
		"editable"            	"1"
		"maxchars"            	"128"
		"NumericInputOnly"    	"1"
		"unicode"             	"1"
		"fgcolor_override"    	"LtText"
		"bgcolor_override"    	"LtButtonHover"
		"paintbackgroundtype" 	"2"
		"font"                	"ImportToolSmallest"
	}
	"SelfIllumLabel"
	{
		"ControlName"      	"CExLabel"
		"fieldName"        	"SelfIllumLabel"
		"font"             	"ImportToolSmallestBold"
		"textAlignment"    	"east"
		"labelText"        	"Self Illumination"
		"xpos"             	"c-100"
		"ypos"             	"360"
		"zpos"             	"0"
		"wide"             	"100"
		"tall"             	"15"
		"fgcolor_override" 	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"SelfIllumCheckButton"
	{
		"ControlName"               	"CheckButton"
		"fieldName"                 	"SelfIllumCheckButton"
		"labelText"                 	""
		"Font"                      	"ImportToolSmallestBold"
		"textAlignment"             	"west"
		"xpos"                      	"c+1"
		"ypos"                      	"357"
		"wide"                      	"30"
		"tall"                      	"20"
		"autoResize"                	"0"
		"pinCorner"                 	"0"
		"visible"                   	"1"
		"enabled"                   	"1"
		"dulltext"                  	"0"
		"brighttext"                	"0"
		"command"                   	"UpdateSelfIllum"
		"border"                    	"SteamWorkshopBorder"
		"fgcolor_override"          	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
		"defaultBgColor_override"   	"LtCardAlt"	// ClaudeHUD: riempimento al posto del bordo texture
		"armedBgColor_override"     	"LtButtonHover"	// ClaudeHUD: riempimento al posto del bordo texture
		"depressedBgColor_override" 	"LtButtonHover"	// ClaudeHUD: riempimento al posto del bordo texture
		"defaultFgColor_override"   	"LtText"	// ClaudeHUD: riempimento al posto del bordo texture
		"armedFgColor_override"     	"LtOnButtonHover"	// ClaudeHUD: riempimento al posto del bordo texture
		"depressedFgColor_override" 	"LtOnButtonHover"	// ClaudeHUD: riempimento al posto del bordo texture
	}
	"SelfIllumTextureBrowse"
	{
		"ControlName"               	"CExImageButton"
		"fieldName"                 	"SelfIllumTextureBrowse"
		"xpos"                      	"c-121"
		"ypos"                      	"380"
		"zpos"                      	"1"
		"wide"                      	"19"
		"tall"                      	"15"
		"autoResize"                	"0"
		"textinsetx"                	"15"
		"use_proportional_insets"   	"1"
		"font"                      	"HudFontSmallBold"
		"textAlignment"             	"west"
		"labelText"                 	""
		"command"                   	"BrowseSelfIllumTexture"
		"image_drawcolor"           	"20 20 19 255"	// token: LtText
		"image_disabledcolor"       	"20 20 19 255"	// token: LtText
		"SubImage"
		{
			"ControlName" 	"ImagePanel"
			"fieldName"   	"SubImage"
			"xpos"        	"3"
			"ypos"        	"1"
			"zpos"        	"1"
			"wide"        	"13"
			"tall"        	"13"
			"scaleImage"  	"1"
			"image"       	"glyph_workshop_view"
		}
		"defaultFgColor_override"   	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
		"armedFgColor_override"     	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"depressedFgColor_override" 	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"defaultBgColor_override"   	"LtCardAlt"	// ClaudeHUD: colore esplicito in modalita' chiara
		"armedBgColor_override"     	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"depressedBgColor_override" 	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"SelfIllumTextureClear"
	{
		"ControlName"               	"CExImageButton"
		"fieldName"                 	"SelfIllumTextureClear"
		"xpos"                      	"c-100"
		"ypos"                      	"380"
		"wide"                      	"15"
		"tall"                      	"15"
		"autoResize"                	"0"
		"pinCorner"                 	"3"
		"textinsetx"                	"15"
		"use_proportional_insets"   	"1"
		"font"                      	"HudFontSmallBold"
		"textAlignment"             	"west"
		"labelText"                 	""
		"command"                   	"ClearSelfIllumTexture"
		"image_drawcolor"           	"20 20 19 255"	// token: LtText
		"image_disabledcolor"       	"20 20 19 255"	// token: LtText
		"SubImage"
		{
			"ControlName" 	"ImagePanel"
			"fieldName"   	"SubImage"
			"xpos"        	"1"
			"ypos"        	"1"
			"zpos"        	"1"
			"wide"        	"13"
			"tall"        	"13"
			"scaleImage"  	"1"
			"image"       	"glyph_close_X"
		}
		"defaultFgColor_override"   	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
		"armedFgColor_override"     	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"depressedFgColor_override" 	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"defaultBgColor_override"   	"LtCardAlt"	// ClaudeHUD: colore esplicito in modalita' chiara
		"armedBgColor_override"     	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"depressedBgColor_override" 	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"SelfIllumTextureLabel"
	{
		"ControlName"      	"CExLabel"
		"fieldName"        	"SelfIllumTextureLabel"
		"font"             	"ImportToolSmallestBold"
		"textAlignment"    	"east"
		"labelText"        	"Shared Illum Mask"
		"xpos"             	"c-85"
		"ypos"             	"380"
		"zpos"             	"0"
		"wide"             	"85"
		"tall"             	"15"
		"fgcolor_override" 	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"SelfIllumTextureFileLabel"
	{
		"ControlName"      	"Label"
		"fieldName"        	"SelfIllumTextureFileLabel"
		"xpos"             	"c+5"
		"ypos"             	"380"
		"wide"             	"190"
		"tall"             	"15"
		"autoResize"       	"0"
		"pinCorner"        	"0"
		"labelText"        	"#TF_PublishFile_Optional"
		"font"             	"ImportToolSmallest"
		"fillcolor"        	"217 119 87 255"	// token: LtAccent
		"textAlignment"    	"west"
		"fgcolor_override" 	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"SelfIllumTintLabel"
	{
		"ControlName"      	"CExLabel"
		"fieldName"        	"SelfIllumTintLabel"
		"font"             	"ImportToolSmallestBold"
		"textAlignment"    	"east"
		"labelText"        	"Self Illumination Tint"
		"xpos"             	"c-150"
		"ypos"             	"400"
		"zpos"             	"0"
		"wide"             	"150"
		"tall"             	"15"
		"enabled"          	"0"
		"fgcolor_override" 	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"SelfIllumTintRedTextEntry"
	{
		"ControlName"         	"TextEntry"
		"fieldName"           	"SelfIllumTintRedTextEntry"
		"xpos"                	"c+5"
		"ypos"                	"400"
		"wide"                	"35"
		"tall"                	"12"
		"autoResize"          	"0"
		"pinCorner"           	"0"
		"visible"             	"1"
		"enabled"             	"0"
		"tabPosition"         	"1"
		"textHidden"          	"0"
		"editable"            	"1"
		"maxchars"            	"128"
		"NumericInputOnly"    	"1"
		"unicode"             	"1"
		"fgcolor_override"    	"LtText"
		"bgcolor_override"    	"LtButtonHover"
		"paintbackgroundtype" 	"2"
		"font"                	"ImportToolSmallest"
	}
	"SelfIllumTintGreenTextEntry"
	{
		"ControlName"         	"TextEntry"
		"fieldName"           	"SelfIllumTintGreenTextEntry"
		"xpos"                	"c+45"
		"ypos"                	"400"
		"wide"                	"35"
		"tall"                	"12"
		"autoResize"          	"0"
		"pinCorner"           	"0"
		"visible"             	"1"
		"enabled"             	"0"
		"tabPosition"         	"1"
		"textHidden"          	"0"
		"editable"            	"1"
		"maxchars"            	"128"
		"NumericInputOnly"    	"1"
		"unicode"             	"1"
		"fgcolor_override"    	"LtText"
		"bgcolor_override"    	"LtButtonHover"
		"paintbackgroundtype" 	"2"
		"font"                	"ImportToolSmallest"
	}
	"SelfIllumTintBlueTextEntry"
	{
		"ControlName"         	"TextEntry"
		"fieldName"           	"SelfIllumTintBlueTextEntry"
		"xpos"                	"c+85"
		"ypos"                	"400"
		"wide"                	"35"
		"tall"                	"12"
		"autoResize"          	"0"
		"pinCorner"           	"0"
		"visible"             	"1"
		"enabled"             	"0"
		"tabPosition"         	"1"
		"textHidden"          	"0"
		"editable"            	"1"
		"maxchars"            	"128"
		"NumericInputOnly"    	"1"
		"unicode"             	"1"
		"fgcolor_override"    	"LtText"
		"bgcolor_override"    	"LtButtonHover"
		"paintbackgroundtype" 	"2"
		"font"                	"ImportToolSmallest"
	}
	"ButtonDone"
	{
		"ControlName"               	"Button"
		"fieldName"                 	"ButtonDone"
		"xpos"                      	"c-175"
		"ypos"                      	"420"
		"wide"                      	"175"
		"tall"                      	"25"
		"autoResize"                	"0"
		"pinCorner"                 	"0"
		"visible"                   	"1"
		"enabled"                   	"1"
		"tabPosition"               	"0"
		"labelText"                 	"#GameUI_OK"
		"textAlignment"             	"center"
		"dulltext"                  	"0"
		"brighttext"                	"0"
		"wrap"                      	"0"
		"Command"                   	"Done"
		"Default"                   	"0"
		"font"                      	"HudFontSmallBold"
		"defaultFgColor_override"   	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
		"armedFgColor_override"     	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"depressedFgColor_override" 	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"defaultBgColor_override"   	"LtCardAlt"	// ClaudeHUD: colore esplicito in modalita' chiara
		"armedBgColor_override"     	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"depressedBgColor_override" 	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
	"ButtonClose"
	{
		"ControlName"               	"Button"
		"fieldName"                 	"ButtonClose"
		"xpos"                      	"c+5"
		"ypos"                      	"420"
		"wide"                      	"175"
		"tall"                      	"25"
		"autoResize"                	"0"
		"pinCorner"                 	"0"
		"visible"                   	"1"
		"enabled"                   	"1"
		"tabPosition"               	"0"
		"labelText"                 	"#Cancel"
		"textAlignment"             	"center"
		"dulltext"                  	"0"
		"brighttext"                	"0"
		"wrap"                      	"0"
		"Command"                   	"Close"
		"Default"                   	"0"
		"font"                      	"HudFontSmallBold"
		"defaultFgColor_override"   	"LtText"	// ClaudeHUD: colore esplicito in modalita' chiara
		"armedFgColor_override"     	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"depressedFgColor_override" 	"LtOnButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"defaultBgColor_override"   	"LtCardAlt"	// ClaudeHUD: colore esplicito in modalita' chiara
		"armedBgColor_override"     	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
		"depressedBgColor_override" 	"LtButtonHover"	// ClaudeHUD: colore esplicito in modalita' chiara
	}
}
