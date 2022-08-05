import yWp8YWaB4m5N2glpnses as app
import time
import ConfigParser
import a70273956fae196f1954b9fb6066a39df as player
import localeInfo
import ui
import e120e808bbd36072fe6d48de1d0c4287e as net
import dbg

def GetName():
	return player.GetChrName().replace("[", '').replace("]", '')

RUNE_DIR_PATH = "d:/ymir work/runes/"
CONFIG_GLOBAL = "%s_global" % (GetName())
CONFIG_SET = "%s_set_%d"
Page_names = ["pvp", "pvm", "support"]

Data = {
	0:{
		"info":{
			"title":{
				"text": localeInfo.RUNE_TEXT_00,
				"color": 0xff9a2422,
				"position":{
					"x": 80 + 60,
					"y": 30,
				},
			},
			"bonus":{
				"text1": "",
				"text2": "",
				"text3": "",
				"text4": "",
				"text5": "",
				"color": 0xff75392d,
				"position":{
					"x": 80 + 60,
					"y": 30 + 15,
				},
			},
		},
		"background": RUNE_DIR_PATH + "rune_page/pvp/bg_pvp.tga",
		"icon":{
			"image": RUNE_DIR_PATH + "rune_page/pvp/pvp_icon.tga",
			"background": RUNE_DIR_PATH + "rune_page/pvp/main_icon_bg_red.tga",
			"position":{
				"icon":{
					"x": 26,
					"y": 30,
				},
				"background":{
					"x": 30,
					"y": 20,
				},
			},
		},
		"keystone_bg": RUNE_DIR_PATH + "rune_page/pvp/keystone_icon_bg.tga",
		"circle":{
			"disabled": RUNE_DIR_PATH + "rune_page/pvp/icon_bg_red01.tga",
			"hover": RUNE_DIR_PATH + "rune_page/pvp/icon_bg_red02.tga",
			"active": RUNE_DIR_PATH + "rune_page/pvp/icon_bg_red03.tga",
			"height": 72,
		},
		"connect":{
			"active": RUNE_DIR_PATH + "rune_page/pvp/connce_red02.tga",
			"inactive": RUNE_DIR_PATH + "rune_page/pvp/connec_red01.tga",
			"height": 46,
		},
		"secondary":{
			"icon":{
				"disabled": RUNE_DIR_PATH + "rune_page/secondary_runes/pvp01.tga",
				"hover": RUNE_DIR_PATH + "rune_page/secondary_runes/pvp02.tga",
				"active": RUNE_DIR_PATH + "rune_page/secondary_runes/pvp03.tga",
				"size":{
					"width": 33,
					"height": 35,
				},
			},
		},
	},
	1:{
		"info":{
			"title":{
				"text": localeInfo.RUNE_TEXT_01,
				"color": 0xffca8a15,
				"position":{
					"x": 80 + 60,
					"y": 30,
				},
			},
			"bonus":{
				"text1": "",
				"text2": "",
				"text3": "",
				"text4": "",
				"text5": "",
				"color": 0xff925b0a,
				"position":{
					"x": 80 + 60,
					"y": 30 + 15,
				},
			},
		},
		"background": RUNE_DIR_PATH + "rune_page/pvm/bg_pvm.tga",
		"icon":{
			"image": RUNE_DIR_PATH + "rune_page/pvm/icon_pvm.tga",
			"background": RUNE_DIR_PATH + "rune_page/pvm/main_icon_bg_gold.tga",
			"position":{
				"icon":{
					"x": 33,
					"y": 30,
				},
				"background":{
					"x": 30,
					"y": 20,
				},
			},
		},
		"keystone_bg": RUNE_DIR_PATH + "rune_page/pvm/keystone_icon_bg_gold.tga",
		"circle":{
			"disabled": RUNE_DIR_PATH + "rune_page/pvm/icon_bg_gold01.tga",
			"hover": RUNE_DIR_PATH + "rune_page/pvm/icon_bg_gold02.tga",
			"active": RUNE_DIR_PATH + "rune_page/pvm/icon_bg_gold03.tga",
			"height": 72,
		},
		"connect":{
			"active": RUNE_DIR_PATH + "rune_page/pvm/connec_gold02.tga",
			"inactive": RUNE_DIR_PATH + "rune_page/pvm/connec_gold01.tga",
			"height": 46,
		},
		"secondary":{
			"icon":{
				"disabled": RUNE_DIR_PATH + "rune_page/secondary_runes/pvm01.tga",
				"hover": RUNE_DIR_PATH + "rune_page/secondary_runes/pvm02.tga",
				"active": RUNE_DIR_PATH + "rune_page/secondary_runes/pvm03.tga",
				"size":{
					"width": 25,
					"height": 35,
				},
			},
		},
	},
	2:{
		"info":{
			"title":{
				"text": localeInfo.RUNE_TEXT_02,
				"color": 0xff3278ca,
				"position":{
					"x": 80 + 60,
					"y": 30,
				},
			},
			"bonus":{
				"text1": "",
				"text2": "",
				"text3": "",
				"text4": "",
				"text5": "",
				"color": 0xff1d5c87,
				"position":{
					"x": 80 + 60,
					"y": 30 + 15,
				},
			},
		},
		"background": RUNE_DIR_PATH + "rune_page/support/bg_supporter.tga",
		"icon":{
			"image": RUNE_DIR_PATH + "rune_page/support/supporter_icon.tga",
			"background": RUNE_DIR_PATH + "rune_page/support/main_icon_bg_blue.tga",
			"position":{
				"icon":{
					"x": 30,
					"y": 30,
				},
				"background":{
					"x": 30,
					"y": 20,
				},
			},
		},
		"keystone_bg": RUNE_DIR_PATH + "rune_page/support/keystone_icon_bg_blue.tga",
		"circle":{
			"disabled": RUNE_DIR_PATH + "rune_page/support/icon_bg_blue01.tga",
			"hover": RUNE_DIR_PATH + "rune_page/support/icon_bg_blue02.tga",
			"active": RUNE_DIR_PATH + "rune_page/support/icon_bg_blue03.tga",
			"height": 72,
		},
		"connect":{
			"active": RUNE_DIR_PATH + "rune_page/support/connec_blue02.tga",
			"inactive": RUNE_DIR_PATH + "rune_page/support/connec_blue01.tga",
			"height": 46,
		},
		"secondary":{
			"icon":{
				"disabled": RUNE_DIR_PATH + "rune_page/secondary_runes/support01.tga",
				"hover": RUNE_DIR_PATH + "rune_page/secondary_runes/support02.tga",
				"active": RUNE_DIR_PATH + "rune_page/secondary_runes/support03.tga",
				"size":{
					"width": 26,
					"height": 35,
				},
			},
		},
	},
}

Runes = {
	0:{
		1:{
			"title": localeInfo.RUNE_TEXT_03,
			"bonus": localeInfo.RUNE_TEXT_04,
		},
		2:{
			"title": localeInfo.RUNE_TEXT_05,
			"bonus": localeInfo.RUNE_TEXT_06,
		},
		3:{
			"title": localeInfo.RUNE_TEXT_07,
			"bonus": localeInfo.RUNE_TEXT_08,
		},
		4:{
			"title": localeInfo.RUNE_TEXT_09,
			"bonus": localeInfo.RUNE_TEXT_10,
		},
		5:{
			"title": localeInfo.RUNE_TEXT_11,
			"bonus": localeInfo.RUNE_TEXT_12,
		},
		6:{
			"title": localeInfo.RUNE_TEXT_13,
			"bonus": localeInfo.RUNE_TEXT_14,
		},
		7:{
			"title": localeInfo.RUNE_TEXT_15,
			"bonus": localeInfo.RUNE_TEXT_16,
		},
		8:{
			"title": localeInfo.RUNE_TEXT_17,
			"bonus": localeInfo.RUNE_TEXT_18,
		},
		9:{
			"title": localeInfo.RUNE_TEXT_19,
			"bonus": localeInfo.RUNE_TEXT_20,
		},	
		10:{
			"title": localeInfo.RUNE_TEXT_21,
			"bonus": localeInfo.RUNE_TEXT_22,
		},
		11:{
			"title": localeInfo.RUNE_TEXT_23,
			"bonus": localeInfo.RUNE_TEXT_24,
		},
		12:{
			"title": localeInfo.RUNE_TEXT_25,
			"bonus": localeInfo.RUNE_TEXT_26,
		},
	},
	1:{
		1:{
			"title": localeInfo.RUNE_TEXT_27,
			"bonus": localeInfo.RUNE_TEXT_28,
		},
		2:{
			"title": localeInfo.RUNE_TEXT_29,
			"bonus": localeInfo.RUNE_TEXT_30,
		},
		3:{
			"title": localeInfo.RUNE_TEXT_31,
			"bonus": localeInfo.RUNE_TEXT_32,
		},
		4:{
			"title": localeInfo.RUNE_TEXT_33,
			"bonus": localeInfo.RUNE_TEXT_34,
		},
		5:{
			"title": localeInfo.RUNE_TEXT_35,
			"bonus": localeInfo.RUNE_TEXT_36,
		},
		6:{
			"title": localeInfo.RUNE_TEXT_37,
			"bonus": localeInfo.RUNE_TEXT_38,
		},
		7:{
			"title": localeInfo.RUNE_TEXT_39,
			"bonus": localeInfo.RUNE_TEXT_40,
		},
		8:{
			"title": localeInfo.RUNE_TEXT_41,
			"bonus": localeInfo.RUNE_TEXT_42,
		},
		9:{
			"title": localeInfo.RUNE_TEXT_43,
			"bonus": localeInfo.RUNE_TEXT_44,
		},	
		10:{
			"title": localeInfo.RUNE_TEXT_45,
			"bonus": localeInfo.RUNE_TEXT_46,
		},
		11:{
			"title": localeInfo.RUNE_TEXT_47,
			"bonus": localeInfo.RUNE_TEXT_48,
		},
		12:{
			"title": localeInfo.RUNE_TEXT_49,
			"bonus": localeInfo.RUNE_TEXT_50,
		},
	},
	2:{
		1:{
			"title": localeInfo.RUNE_TEXT_51,
			"bonus": localeInfo.RUNE_TEXT_52,
		},
		2:{
			"title": localeInfo.RUNE_TEXT_53,
			"bonus": localeInfo.RUNE_TEXT_54,
		},
		3:{
			"title": localeInfo.RUNE_TEXT_55,
			"bonus": localeInfo.RUNE_TEXT_56,
		},
		4:{
			"title": localeInfo.RUNE_TEXT_57,
			"bonus": localeInfo.RUNE_TEXT_58,
		},
		5:{
			"title": localeInfo.RUNE_TEXT_59,
			"bonus": localeInfo.RUNE_TEXT_60,
		},
		6:{
			"title": localeInfo.RUNE_TEXT_61,
			"bonus": localeInfo.RUNE_TEXT_62,
		},
		7:{
			"title": localeInfo.RUNE_TEXT_63,
			"bonus": localeInfo.RUNE_TEXT_64,
		},
		8:{
			"title": localeInfo.RUNE_TEXT_65,
			"bonus": localeInfo.RUNE_TEXT_66,
		},
		9:{
			"title": localeInfo.RUNE_TEXT_67,
			"bonus": localeInfo.RUNE_TEXT_68,
		},	
		10:{
			"title": localeInfo.RUNE_TEXT_69,
			"bonus": localeInfo.RUNE_TEXT_70,
		},
		11:{
			"title": localeInfo.RUNE_TEXT_71,
			"bonus": localeInfo.RUNE_TEXT_72,
		},
		12:{
			"title": localeInfo.RUNE_TEXT_73,
			"bonus": localeInfo.RUNE_TEXT_74,
		},
	},
}

class RuneConfig:
	def __init__(self):
		self.config = ConfigParser.ConfigParser()
		self.config.read("lib/encodings/runes.cfg")

	def __del__(self):
		del self.config

	def Save(self):
		with open('lib/encodings/runes.cfg', 'wb') as configfile:
			self.config.write(configfile)
	
	def Get(self, section, variable, default):
		if not self.config.has_section(section):
			self.config.add_section(section)
			self.config.set(section, variable, str(default))
			return int(default)
		else:
			if not self.config.has_option(section, variable):
				self.config.set(section, variable, str(default))
				return int(default)
			else:
				return int(self.config.getint(section, variable))
	
	def Set(self, section, variable, value):
		if not self.config.has_section(section):
			self.config.add_section(section)
		self.config.set(section, variable, str(value))

class RunePage(ui.Board):
	def __init__(self):
		ui.Board.__init__(self)
		# if app.ENABLE_WINDOW_SLIDE_EFFECT:
			# self.EnableSlidingEffect()

		self.wndRunePrincipal = None
		self.CurrentSet = 0
		self.CurrentPage = 0
		self.SecondaryPage = 1
		self.Keystone = 0
		self.Runes = [0, 0, 0, 0, 0]

		self.GUI = {}
		self.GUI["keystone"] = {}
		self.GUI["keystone"]["selection"] = {0:{}, 1:{}, 2:{}}
		self.GUI["runes"] = {0:{}, 1:{}, 2:{}, 3:{}, 4:{}, 5:{}, 6:{}}
		self.GUI["PAGE_BONUSES_PRINCIPAL"] = [0, 0, 0, 0, 0]
		self.GUI["PAGE_BONUSES_SECONDARY"] = [0, 0, 0]
		self.GUI["PAGE_SET"] = [0, 0, 0, 0, 0]
		self.GUI["seconadaries"] = [0, 0, 0]
		
		self.SetSize(800 + 13, 600 + 13)
		self.SetCenterPosition()
		# self.AddFlag("movable")
		# self.AddFlag("float")
		self.Hide()
		
		self.GUI["background"] = ui.ExpandedImageBox()
		self.GUI["background"].SetParent(self)
		self.GUI["background"].SetPosition(5, 5)
		self.GUI["background"].SetSize(800, 600)
		self.GUI["background"].AddFlag("not_pick")
		self.GUI["background"].LoadImage(Data[self.CurrentPage]["background"])
		self.GUI["background"].Show()
		
		self.GUI["save"] = ui.Button()
		self.GUI["save"].SetParent(self)
		self.GUI["save"].SetPosition(670, 20)
		self.GUI["save"].SetSize(34, 36)
		self.GUI["save"].SetUpVisual(RUNE_DIR_PATH + "rune_page/top_icons/save01.tga")
		self.GUI["save"].SetOverVisual(RUNE_DIR_PATH + "rune_page/top_icons/save02.tga")
		self.GUI["save"].SetDownVisual(RUNE_DIR_PATH + "rune_page/top_icons/save03.tga")
		self.GUI["save"].SetEvent(ui.mem_func(self.Save))
		self.GUI["save"].Show()
		
		self.GUI["delete"] = ui.Button()
		self.GUI["delete"].SetParent(self)
		self.GUI["delete"].SetPosition(670 + 44, 20)
		self.GUI["delete"].SetSize(31, 37)
		self.GUI["delete"].SetUpVisual(RUNE_DIR_PATH + "rune_page/top_icons/trash01.tga")
		self.GUI["delete"].SetOverVisual(RUNE_DIR_PATH + "rune_page/top_icons/trash02.tga")
		self.GUI["delete"].SetDownVisual(RUNE_DIR_PATH + "rune_page/top_icons/trash03.tga")
		self.GUI["delete"].SetEvent(ui.mem_func(self.Delete))
		self.GUI["delete"].Show()
		
		self.GUI["back"] = ui.Button()
		self.GUI["back"].SetParent(self)
		self.GUI["back"].SetPosition(670 + 85, 25)
		self.GUI["back"].SetSize(34, 28)
		self.GUI["back"].SetUpVisual(RUNE_DIR_PATH + "rune_page/top_icons/back01.tga")
		self.GUI["back"].SetOverVisual(RUNE_DIR_PATH + "rune_page/top_icons/back02.tga")
		self.GUI["back"].SetDownVisual(RUNE_DIR_PATH + "rune_page/top_icons/back03.tga")
		self.GUI["back"].SetEvent(ui.mem_func(self.Back))
		self.GUI["back"].Show()
		
		self.GUI["keystone"]["connector"] = ui.ImageBox()
		self.GUI["keystone"]["connector"].SetParent(self)
		self.GUI["keystone"]["connector"].SetPosition(84, 158)
		self.GUI["keystone"]["connector"].LoadImage(Data[self.CurrentPage]["connect"]["inactive"])
		self.GUI["keystone"]["connector"].Show()
		
		for i in range(3):
			self.GUI["runes"][i]["connector"] = ui.ImageBox()
			self.GUI["runes"][i]["connector"].SetParent(self)
			self.GUI["runes"][i]["connector"].SetPosition(84, 158 + (50 + Data[self.CurrentPage]["connect"]["height"]) * (i + 1))
			self.GUI["runes"][i]["connector"].LoadImage(Data[self.CurrentPage]["connect"]["inactive"])
			self.GUI["runes"][i]["connector"].Show()
			
		for x in range(2):
			i = x + 3
			self.GUI["runes"][i]["connector"] = ui.ImageBox()
			self.GUI["runes"][i]["connector"].SetParent(self)
			self.GUI["runes"][i]["connector"].SetPosition(480, 150 + 120 + (50 + Data[self.SecondaryPage]["connect"]["height"]) * x)
			self.GUI["runes"][i]["connector"].LoadImage(Data[self.SecondaryPage]["connect"]["inactive"])
			self.GUI["runes"][i]["connector"].Show()
		
		self.GUI["keystone"]["bg"] = ui.Button()
		self.GUI["keystone"]["bg"].SetParent(self)
		self.GUI["keystone"]["bg"].SetPosition(50, 190)
		self.GUI["keystone"]["bg"].SetUpVisual(Data[self.CurrentPage]["keystone_bg"])
		self.GUI["keystone"]["bg"].SetOverVisual(Data[self.CurrentPage]["keystone_bg"])
		self.GUI["keystone"]["bg"].SetDownVisual(Data[self.CurrentPage]["keystone_bg"])
		self.GUI["keystone"]["bg"].SetEvent(ui.mem_func(self.ClickKeystone))
		self.GUI["keystone"]["bg"].Show()
		
		self.GUI["keystone"]["icon"] = ui.ImageBox()
		self.GUI["keystone"]["icon"].SetParent(self)
		self.GUI["keystone"]["icon"].SetPosition(58, 195)
		self.GUI["keystone"]["icon"].AddFlag("not_pick")
		self.GUI["keystone"]["icon"].LoadImage(RUNE_DIR_PATH + "rune_page/rune_icons/pvp/keystone1.sub")
		self.GUI["keystone"]["icon"].Hide()
		
		self.GUI["keystone"]["title"] = ui.TextLine()
		self.GUI["keystone"]["title"].SetParent(self)
		self.GUI["keystone"]["title"].SetPosition(Data[self.CurrentPage]["icon"]["position"]["background"]["x"] + Data[self.CurrentPage]["info"]["title"]["position"]["x"] - 25, 205)
		self.GUI["keystone"]["title"].SetFontName("Arial:16")
		self.GUI["keystone"]["title"].SetPackedFontColor(Data[self.CurrentPage]["info"]["title"]["color"])
		self.GUI["keystone"]["title"].SetText(localeInfo.RUNE_TEXT_75)
		self.GUI["keystone"]["title"].Show()
		
		self.GUI["keystone"]["text"] = ui.TextLine()
		self.GUI["keystone"]["text"].SetParent(self)
		self.GUI["keystone"]["text"].SetPosition(Data[self.CurrentPage]["icon"]["position"]["background"]["x"] + Data[self.CurrentPage]["info"]["title"]["position"]["x"] - 25, 225)
		self.GUI["keystone"]["text"].SetFontName("Arial:12")
		self.GUI["keystone"]["text"].SetPackedFontColor(Data[self.CurrentPage]["info"]["bonus"]["color"])
		self.GUI["keystone"]["text"].SetText(localeInfo.RUNE_TEXT_76)
		self.GUI["keystone"]["text"].Show()
		
		for i in range(3):
			self.GUI["seconadaries"][i] = ui.Button()
			self.GUI["seconadaries"][i].SetParent(self)
			self.GUI["seconadaries"][i].SetPosition(590 + (35 + 20) * i, 140)
			self.GUI["seconadaries"][i].SetSize(Data[i]["secondary"]["icon"]["size"]["width"], Data[i]["secondary"]["icon"]["size"]["height"])
			self.GUI["seconadaries"][i].SetUpVisual(Data[i]["secondary"]["icon"]["disabled"])
			self.GUI["seconadaries"][i].SetOverVisual(Data[i]["secondary"]["icon"]["hover"])
			self.GUI["seconadaries"][i].SetDownVisual(Data[i]["secondary"]["icon"]["active"])
			self.GUI["seconadaries"][i].SetDisableVisual(Data[i]["secondary"]["icon"]["active"])
			self.GUI["seconadaries"][i].SetEvent(ui.mem_func(self.SelectSecondary), i)
			self.GUI["seconadaries"][i].Show()
		
		for i in range(3):
			self.GUI["keystone"]["selection"][i] = ui.Button()
			self.GUI["keystone"]["selection"][i].SetParent(self)
			self.GUI["keystone"]["selection"][i].SetPosition(30 + 15 + 5 + 40 + 75 * (i + 1), 194 - 10 + 10)
			self.GUI["keystone"]["selection"][i].SetSize(85, 85)
			self.GUI["keystone"]["selection"][i].SetUpVisual(RUNE_DIR_PATH + "rune_page/rune_icons/%s/keystone%d.sub" % (Page_names[self.CurrentPage], i + 1))
			self.GUI["keystone"]["selection"][i].SetDownVisual(RUNE_DIR_PATH + "rune_page/rune_icons/%s/keystone%d.sub" % (Page_names[self.CurrentPage], i + 1))
			self.GUI["keystone"]["selection"][i].SetOverVisual(RUNE_DIR_PATH + "rune_page/rune_icons/%s/keystone%d.sub" % (Page_names[self.CurrentPage], i + 1))
			self.GUI["keystone"]["selection"][i].SetToolTipText(Runes[self.CurrentPage][i + 1]["bonus"])
			self.GUI["keystone"]["selection"][i].SetEvent(ui.mem_func(self.SelectKeystone), i + 1)
			self.GUI["keystone"]["selection"][i].Show()
		
		for i in range(3):
			self.GUI["runes"][i]["selection"] = {0:{}, 1:{}, 2:{}}
			self.GUI["runes"][i]["bg"] = ui.Button()
			self.GUI["runes"][i]["bg"].SetParent(self)
			self.GUI["runes"][i]["bg"].SetPosition(60, 205 + ((Data[self.CurrentPage]["connect"]["height"] / 2) + Data[self.CurrentPage]["circle"]["height"] ) * (i + 1))
			self.GUI["runes"][i]["bg"].SetUpVisual(Data[self.CurrentPage]["circle"]["disabled"])
			self.GUI["runes"][i]["bg"].SetOverVisual(Data[self.CurrentPage]["circle"]["hover"])
			self.GUI["runes"][i]["bg"].SetDownVisual(Data[self.CurrentPage]["circle"]["active"])
			self.GUI["runes"][i]["bg"].SetEvent(ui.mem_func(self.ClickRune), i)
			self.GUI["runes"][i]["bg"].Show()
			
			self.GUI["runes"][i]["icon"] = ui.ImageBox()
			self.GUI["runes"][i]["icon"].SetParent(self)
			self.GUI["runes"][i]["icon"].SetPosition(60 - 1, 205 + ((Data[self.CurrentPage]["connect"]["height"] / 2) + Data[self.CurrentPage]["circle"]["height"] ) * (i + 1) - 3)
			self.GUI["runes"][i]["icon"].AddFlag("not_pick")
			self.GUI["runes"][i]["icon"].LoadImage(RUNE_DIR_PATH + "rune_page/rune_icons/pvp/keystone1.sub")
			self.GUI["runes"][i]["icon"].Hide()
			
			self.GUI["runes"][i]["title"] = ui.TextLine()
			self.GUI["runes"][i]["title"].SetParent(self)
			self.GUI["runes"][i]["title"].SetPosition(Data[self.CurrentPage]["icon"]["position"]["background"]["x"] + Data[self.CurrentPage]["info"]["title"]["position"]["x"] - 25, 205 + ((Data[self.CurrentPage]["connect"]["height"] / 2) + Data[self.CurrentPage]["circle"]["height"] ) * (i+1))
			self.GUI["runes"][i]["title"].SetFontName("Arial:16")
			self.GUI["runes"][i]["title"].SetPackedFontColor(Data[self.CurrentPage]["info"]["title"]["color"])
			self.GUI["runes"][i]["title"].SetText(localeInfo.RUNE_TEXT_77)
			self.GUI["runes"][i]["title"].Show()
			
			self.GUI["runes"][i]["text"] = ui.TextLine()
			self.GUI["runes"][i]["text"].SetParent(self)
			self.GUI["runes"][i]["text"].SetPosition(Data[self.CurrentPage]["icon"]["position"]["background"]["x"] + Data[self.CurrentPage]["info"]["title"]["position"]["x"] - 25, 225 + ((Data[self.CurrentPage]["connect"]["height"] / 2) + Data[self.CurrentPage]["circle"]["height"] ) * (i+1))
			self.GUI["runes"][i]["text"].SetFontName("Arial:12")
			self.GUI["runes"][i]["text"].SetPackedFontColor(Data[self.CurrentPage]["info"]["bonus"]["color"])
			self.GUI["runes"][i]["text"].SetText(localeInfo.RUNE_TEXT_78)
			self.GUI["runes"][i]["text"].Show()
			
			for j in range(3):
				self.GUI["runes"][i]["selection"][j] = ui.Button()
				self.GUI["runes"][i]["selection"][j].SetParent(self)
				self.GUI["runes"][i]["selection"][j].SetPosition(30 + 15 + 5 + 40 + 30 + 40 + 75 * (j), 325 - 10 - 5 - 10 + (46 + 72 - 30)*(i))
				self.GUI["runes"][i]["selection"][j].SetSize(85, 85)
				self.GUI["runes"][i]["selection"][j].SetUpVisual(RUNE_DIR_PATH + "rune_page/rune_icons/%s/rune%d.sub" % (Page_names[self.CurrentPage], 3 * i  + j + 1))
				self.GUI["runes"][i]["selection"][j].SetDownVisual(RUNE_DIR_PATH + "rune_page/rune_icons/%s/rune%d.sub" % (Page_names[self.CurrentPage], 3 * i  + j + 1))
				self.GUI["runes"][i]["selection"][j].SetOverVisual(RUNE_DIR_PATH + "rune_page/rune_icons/%s/rune%d.sub" % (Page_names[self.CurrentPage], 3 * i  + j + 1))
				self.GUI["runes"][i]["selection"][j].SetToolTipText(Runes[self.CurrentPage][3 * i + j + 1]["bonus"])
				self.GUI["runes"][i]["selection"][j].SetEvent(ui.mem_func(self.SelectRune), i, 3 * i  + j + 1)
				self.GUI["runes"][i]["selection"][j].Hide()
			
		
		self.GUI["PAGE_IMAGE_PRINCIPAL"] = ui.ImageBox()
		self.GUI["PAGE_IMAGE_PRINCIPAL"].SetParent(self)
		self.GUI["PAGE_IMAGE_PRINCIPAL"].SetPosition(Data[self.CurrentPage]["icon"]["position"]["background"]["x"], Data[self.CurrentPage]["icon"]["position"]["background"]["y"])
		self.GUI["PAGE_IMAGE_PRINCIPAL"].LoadImage(Data[self.CurrentPage]["icon"]["background"])
		self.GUI["PAGE_IMAGE_PRINCIPAL"].Show()
		
		self.GUI["PAGE_ICON_PRINCIPAL"] = ui.ImageBox()
		self.GUI["PAGE_ICON_PRINCIPAL"].SetParent(self)
		self.GUI["PAGE_ICON_PRINCIPAL"].SetPosition(Data[self.CurrentPage]["icon"]["position"]["background"]["x"] + Data[self.CurrentPage]["icon"]["position"]["icon"]["x"], Data[self.CurrentPage]["icon"]["position"]["background"]["y"] + Data[self.CurrentPage]["icon"]["position"]["icon"]["y"])
		self.GUI["PAGE_ICON_PRINCIPAL"].LoadImage(Data[self.CurrentPage]["icon"]["image"])
		self.GUI["PAGE_ICON_PRINCIPAL"].Show()
		
		self.GUI["PAGE_TITLE_PRINCIPAL"] = ui.TextLine()
		self.GUI["PAGE_TITLE_PRINCIPAL"].SetParent(self)
		self.GUI["PAGE_TITLE_PRINCIPAL"].SetPosition(Data[self.CurrentPage]["icon"]["position"]["background"]["x"] + Data[self.CurrentPage]["info"]["title"]["position"]["x"], Data[self.CurrentPage]["icon"]["position"]["background"]["y"] + Data[self.CurrentPage]["info"]["title"]["position"]["y"])
		self.GUI["PAGE_TITLE_PRINCIPAL"].SetFontName("Arial:18")
		self.GUI["PAGE_TITLE_PRINCIPAL"].SetPackedFontColor(Data[self.CurrentPage]["info"]["title"]["color"])
		self.GUI["PAGE_TITLE_PRINCIPAL"].SetText(Data[self.CurrentPage]["info"]["title"]["text"])
		self.GUI["PAGE_TITLE_PRINCIPAL"].Show()
		
		self.GUI["PAGE_IMAGE_SECONDARY"] = ui.ImageBox()
		self.GUI["PAGE_IMAGE_SECONDARY"].SetParent(self)
		self.GUI["PAGE_IMAGE_SECONDARY"].SetPosition(430, 150)
		self.GUI["PAGE_IMAGE_SECONDARY"].LoadImage(Data[self.SecondaryPage]["icon"]["background"])
		self.GUI["PAGE_IMAGE_SECONDARY"].Show()
		
		self.GUI["PAGE_ICON_SECONDARY"] = ui.ImageBox()
		self.GUI["PAGE_ICON_SECONDARY"].SetParent(self)
		self.GUI["PAGE_ICON_SECONDARY"].SetPosition(430 + Data[self.SecondaryPage]["icon"]["position"]["icon"]["x"], 150 + Data[self.SecondaryPage]["icon"]["position"]["icon"]["y"])
		self.GUI["PAGE_ICON_SECONDARY"].LoadImage(Data[self.SecondaryPage]["icon"]["image"])
		self.GUI["PAGE_ICON_SECONDARY"].Show()
		
		self.GUI["PAGE_TITLE_SECONDARY"] = ui.TextLine()
		self.GUI["PAGE_TITLE_SECONDARY"].SetParent(self)
		self.GUI["PAGE_TITLE_SECONDARY"].SetPosition(430 + Data[self.SecondaryPage]["info"]["title"]["position"]["x"], 150 + Data[self.SecondaryPage]["info"]["title"]["position"]["y"])
		self.GUI["PAGE_TITLE_SECONDARY"].SetFontName("Arial:18")
		self.GUI["PAGE_TITLE_SECONDARY"].SetPackedFontColor(Data[self.SecondaryPage]["info"]["title"]["color"])
		self.GUI["PAGE_TITLE_SECONDARY"].SetText(Data[self.SecondaryPage]["info"]["title"]["text"])
		self.GUI["PAGE_TITLE_SECONDARY"].Show()
		
		for x in range(2):
			i = x + 3
			self.GUI["runes"][i]["selection"] = {0:{}, 1:{}, 2:{},}
			self.GUI["runes"][i]["bg"] = ui.Button()
			self.GUI["runes"][i]["bg"].SetParent(self)
			self.GUI["runes"][i]["bg"].SetPosition(455, 150 + 120 + 35 + ((Data[self.SecondaryPage]["connect"]["height"] / 2) + Data[self.SecondaryPage]["circle"]["height"] ) * x)
			self.GUI["runes"][i]["bg"].SetUpVisual(Data[self.SecondaryPage]["circle"]["disabled"])
			self.GUI["runes"][i]["bg"].SetOverVisual(Data[self.SecondaryPage]["circle"]["hover"])
			self.GUI["runes"][i]["bg"].SetDownVisual(Data[self.SecondaryPage]["circle"]["active"])
			self.GUI["runes"][i]["bg"].SetEvent(ui.mem_func(self.ClickRune), i)
			self.GUI["runes"][i]["bg"].Show()
			
			self.GUI["runes"][i]["icon"] = ui.ImageBox()
			self.GUI["runes"][i]["icon"].SetParent(self)
			self.GUI["runes"][i]["icon"].SetPosition(455 - 1, 150 + 120 + 35 + ((Data[self.SecondaryPage]["connect"]["height"] / 2) + Data[self.SecondaryPage]["circle"]["height"] ) * x - 3)
			self.GUI["runes"][i]["icon"].AddFlag("not_pick")
			self.GUI["runes"][i]["icon"].LoadImage(RUNE_DIR_PATH + "rune_page/rune_icons/pvp/keystone1.sub")
			self.GUI["runes"][i]["icon"].Show()
			
			self.GUI["runes"][i]["title"] = ui.TextLine()
			self.GUI["runes"][i]["title"].SetParent(self)
			self.GUI["runes"][i]["title"].SetPosition(455 + Data[self.SecondaryPage]["info"]["title"]["position"]["x"] - 50, 215 + ((Data[self.SecondaryPage]["connect"]["height"] / 2) + Data[self.SecondaryPage]["circle"]["height"] ) * (x + 1))
			self.GUI["runes"][i]["title"].SetFontName("Arial:16")
			self.GUI["runes"][i]["title"].SetPackedFontColor(Data[self.SecondaryPage]["info"]["title"]["color"])
			self.GUI["runes"][i]["title"].SetText(localeInfo.RUNE_TEXT_77)
			self.GUI["runes"][i]["title"].Show()
			
			self.GUI["runes"][i]["text"] = ui.TextLine()
			self.GUI["runes"][i]["text"].SetParent(self)
			self.GUI["runes"][i]["text"].SetPosition(455 + Data[self.SecondaryPage]["info"]["title"]["position"]["x"] - 50, 235 + ((Data[self.SecondaryPage]["connect"]["height"] / 2) + Data[self.SecondaryPage]["circle"]["height"] ) * (x + 1))
			self.GUI["runes"][i]["text"].SetFontName("Arial:12")
			self.GUI["runes"][i]["text"].SetPackedFontColor(Data[self.SecondaryPage]["info"]["bonus"]["color"])
			self.GUI["runes"][i]["text"].SetText(localeInfo.RUNE_TEXT_78)
			self.GUI["runes"][i]["text"].Show()
			
			for j in range(3):
				self.GUI["runes"][i]["selection"][j] = ui.Button()
				self.GUI["runes"][i]["selection"][j].SetParent(self)
				self.GUI["runes"][i]["selection"][j].SetPosition(465 + 100 + 70 * j, 325 - 10 - 5 - 10 + (46 + 72 - 30) * x)
				self.GUI["runes"][i]["selection"][j].SetSize(85, 85)
				self.GUI["runes"][i]["selection"][j].SetUpVisual(RUNE_DIR_PATH + "rune_page/rune_icons/%s/rune%d.sub" % (Page_names[self.SecondaryPage], 3 * x  + j + 1))
				self.GUI["runes"][i]["selection"][j].SetDownVisual(RUNE_DIR_PATH + "rune_page/rune_icons/%s/rune%d.sub" % (Page_names[self.SecondaryPage], 3 * x  + j + 1))
				self.GUI["runes"][i]["selection"][j].SetOverVisual(RUNE_DIR_PATH + "rune_page/rune_icons/%s/rune%d.sub" % (Page_names[self.SecondaryPage], 3 * x  + j + 1))
				self.GUI["runes"][i]["selection"][j].SetToolTipText(Runes[self.SecondaryPage][3 + 3 * x + j + 1]["bonus"])
				self.GUI["runes"][i]["selection"][j].SetEvent(ui.mem_func(self.SelectRuneSec), i, 3 * x  + j + 1)
				self.GUI["runes"][i]["selection"][j].Hide()
		
		for j in range(3):
			self.GUI["runes"][4]["selection"][3 + j] = ui.Button()
			self.GUI["runes"][4]["selection"][3 + j].SetParent(self)
			self.GUI["runes"][4]["selection"][3 + j].SetPosition(465 + 100 + 70 * j , 325 - 10 - 5 - 10 + (46 + 72 - 30) * 2)
			self.GUI["runes"][4]["selection"][3 + j].SetSize(85, 85)
			self.GUI["runes"][4]["selection"][3 + j].SetUpVisual(RUNE_DIR_PATH + "rune_page/rune_icons/%s/rune%d.sub" % (Page_names[self.SecondaryPage], 3 * 2  + j + 1))
			self.GUI["runes"][4]["selection"][3 + j].SetDownVisual(RUNE_DIR_PATH + "rune_page/rune_icons/%s/rune%d.sub" % (Page_names[self.SecondaryPage], 3 * 2  +  j + 1))
			self.GUI["runes"][4]["selection"][3 + j].SetOverVisual(RUNE_DIR_PATH + "rune_page/rune_icons/%s/rune%d.sub" % (Page_names[self.SecondaryPage], 3 * 2  + j + 1))
			self.GUI["runes"][4]["selection"][3 + j].SetToolTipText(Runes[self.SecondaryPage][3 + 3 * 2 + j + 1]["bonus"])
			self.GUI["runes"][4]["selection"][3 + j].SetEvent(ui.mem_func(self.SelectRuneSec), 4, 3 * 2  + j + 1)
			self.GUI["runes"][4]["selection"][3 + j].Hide()
				
		for i in range(5):
			self.GUI["PAGE_BONUSES_PRINCIPAL"][i] = ui.TextLine()
			self.GUI["PAGE_BONUSES_PRINCIPAL"][i].SetParent(self)
			self.GUI["PAGE_BONUSES_PRINCIPAL"][i].SetPosition(Data[self.CurrentPage]["icon"]["position"]["background"]["x"] + Data[self.CurrentPage]["info"]["bonus"]["position"]["x"], Data[self.CurrentPage]["icon"]["position"]["background"]["y"] + Data[self.CurrentPage]["info"]["bonus"]["position"]["y"] + 15 * i)
			self.GUI["PAGE_BONUSES_PRINCIPAL"][i].SetFontName("Arial:14")
			self.GUI["PAGE_BONUSES_PRINCIPAL"][i].SetPackedFontColor(Data[self.CurrentPage]["info"]["bonus"]["color"])
			self.GUI["PAGE_BONUSES_PRINCIPAL"][i].SetText(Data[self.CurrentPage]["info"]["bonus"]["text%d" % (i + 1)])
			self.GUI["PAGE_BONUSES_PRINCIPAL"][i].Show()
			
		for i in range(2):
			self.GUI["PAGE_BONUSES_SECONDARY"][i] = ui.TextLine()
			self.GUI["PAGE_BONUSES_SECONDARY"][i].SetParent(self)
			self.GUI["PAGE_BONUSES_SECONDARY"][i].SetPosition(430 + Data[self.CurrentPage]["info"]["bonus"]["position"]["x"], 150 + Data[self.CurrentPage]["info"]["bonus"]["position"]["y"] + 15 * i)
			self.GUI["PAGE_BONUSES_SECONDARY"][i].SetFontName("Arial:14")
			self.GUI["PAGE_BONUSES_SECONDARY"][i].SetPackedFontColor(Data[self.CurrentPage]["info"]["bonus"]["color"])
			self.GUI["PAGE_BONUSES_SECONDARY"][i].SetText(Data[self.CurrentPage]["info"]["bonus"]["text%d" % (i + 1)])
			self.GUI["PAGE_BONUSES_SECONDARY"][i].Show()
			
		for i in range(5):
			self.GUI["PAGE_SET"][i] = ui.Button()
			self.GUI["PAGE_SET"][i].SetParent(self)
			self.GUI["PAGE_SET"][i].SetPosition(600 + 30 * i + 20, 570)
			self.GUI["PAGE_SET"][i].SetSize(9, 9)
			self.GUI["PAGE_SET"][i].SetUpVisual(RUNE_DIR_PATH + "points_images/normal.tga")
			self.GUI["PAGE_SET"][i].SetOverVisual(RUNE_DIR_PATH + "points_images/hover.tga")
			self.GUI["PAGE_SET"][i].SetDownVisual(RUNE_DIR_PATH + "points_images/down.tga")
			self.GUI["PAGE_SET"][i].SetDisableVisual(RUNE_DIR_PATH + "points_images/active.tga")
			self.GUI["PAGE_SET"][i].SetEvent(ui.mem_func(self.SelectSet), i)
			self.GUI["PAGE_SET"][i].Show()
		
	def __del__(self):
		ui.Board.__del__(self)
	
	def Bind(self, principal):
		self.wndRunePrincipal = principal
	
	def SelectSecondary(self, sec):
		self.SecondaryPage = sec
		self.Configure()
	
	def SelectPage(self, page):
		self.SetCenterPosition()
		self.Show()
		self.Reset()
		self.CurrentPage = page
		self.SecondaryPage = self.GetCorrectSecPage()
		self.Load()
		self.Configure()
	
	def GetCorrectSecPage(self):
		if self.SecondaryPage == self.CurrentPage:
			if self.SecondaryPage == 0:
				return 1
			else:
				return 0
		return self.SecondaryPage
		
	def Load(self):
		if self.CurrentPage == self.wndRunePrincipal.Parser.Get(CONFIG_SET  % (GetName(), self.CurrentSet), "page", 0):
			self.CurrentPage = self.wndRunePrincipal.Parser.Get(CONFIG_SET  % (GetName(), self.CurrentSet), "page", 0)
			self.Keystone = self.wndRunePrincipal.Parser.Get(CONFIG_SET  % (GetName(), self.CurrentSet), "keystone", 0)
			self.SecondaryPage = self.wndRunePrincipal.Parser.Get(CONFIG_SET  % (GetName(), self.CurrentSet), "secondary", 1)
			for i in range(5):
				self.Runes[i] = self.wndRunePrincipal.Parser.Get(CONFIG_SET % (GetName(), self.CurrentSet), "rune%d" % (i + 1), 0)
			self.SecondaryPage = self.GetCorrectSecPage()
			if self.SecondaryPage != self.wndRunePrincipal.Parser.Get(CONFIG_SET  % (GetName(), self.CurrentSet), "secondary", self.GetCorrectSecPage()):
				self.Runes[3] = 0
				self.Runes[4] = 0
	
	def LoadBySet(self):
		self.CurrentPage = self.wndRunePrincipal.Parser.Get(CONFIG_SET  % (GetName(), self.CurrentSet), "page", 0)
		self.Keystone = self.wndRunePrincipal.Parser.Get(CONFIG_SET  % (GetName(), self.CurrentSet), "keystone", 0)
		self.SecondaryPage = self.wndRunePrincipal.Parser.Get(CONFIG_SET  % (GetName(), self.CurrentSet), "secondary", 1)
		for i in range(5):
			self.Runes[i] = self.wndRunePrincipal.Parser.Get(CONFIG_SET % (GetName(), self.CurrentSet), "rune%d" % (i + 1), 0)
		self.SecondaryPage = self.GetCorrectSecPage()
		if self.SecondaryPage != self.wndRunePrincipal.Parser.Get(CONFIG_SET  % (GetName(), self.CurrentSet), "secondary", self.GetCorrectSecPage()):
			self.Runes[3] = 0
			self.Runes[4] = 0
	
	def Open(self, page_set):
		self.CurrentSet = page_set
		self.LoadBySet()
		self.Configure()
		self.Show()
		self.wndRunePrincipal.Board.Hide()
	
	def SelectSet(self, page_set):
		self.CurrentSet = page_set
		self.CurrentPage = self.wndRunePrincipal.Parser.Get(CONFIG_SET  % (GetName(), self.CurrentSet), "page", 0)
		self.SecondaryPage = self.wndRunePrincipal.Parser.Get(CONFIG_SET  % (GetName(), self.CurrentSet), "secondary", 1)
		self.Keystone = self.wndRunePrincipal.Parser.Get(CONFIG_SET  % (GetName(), self.CurrentSet), "keystone", 0)
		for i in range(5):
			self.Runes[i] = self.wndRunePrincipal.Parser.Get(CONFIG_SET % (GetName(), self.CurrentSet), "rune%d" % (i + 1), 0)
		self.Load()
		self.Configure()
	
	def Reset(self):
		self.CurrentPage = 0
		self.Keystone = 0
		self.SecondaryPage = 1
		for i in range(5):
			self.Runes[i] = 0
		self.GUI["keystone"]["icon"].Hide()
		
	def Configure(self):
		self.GUI["background"].LoadImage(Data[self.CurrentPage]["background"])
		self.GUI["PAGE_IMAGE_PRINCIPAL"].LoadImage(Data[self.CurrentPage]["icon"]["background"])
		self.GUI["PAGE_ICON_PRINCIPAL"].LoadImage(Data[self.CurrentPage]["icon"]["image"])
		self.GUI["PAGE_ICON_PRINCIPAL"].SetPosition(Data[self.CurrentPage]["icon"]["position"]["background"]["x"] + Data[self.CurrentPage]["icon"]["position"]["icon"]["x"], Data[self.CurrentPage]["icon"]["position"]["background"]["y"] + Data[self.CurrentPage]["icon"]["position"]["icon"]["y"])
		self.GUI["PAGE_IMAGE_SECONDARY"].LoadImage(Data[self.SecondaryPage]["icon"]["background"])
		self.GUI["PAGE_ICON_SECONDARY"].LoadImage(Data[self.SecondaryPage]["icon"]["image"])
		self.GUI["PAGE_ICON_SECONDARY"].SetPosition(430 + Data[self.SecondaryPage]["icon"]["position"]["icon"]["x"], 150 + Data[self.SecondaryPage]["icon"]["position"]["icon"]["y"])
		self.GUI["keystone"]["bg"].SetUpVisual(Data[self.CurrentPage]["keystone_bg"])
		self.GUI["keystone"]["bg"].SetOverVisual(Data[self.CurrentPage]["keystone_bg"])
		self.GUI["keystone"]["bg"].SetDownVisual(Data[self.CurrentPage]["keystone_bg"])
		self.GUI["PAGE_TITLE_PRINCIPAL"].SetPackedFontColor(Data[self.CurrentPage]["info"]["title"]["color"])
		self.GUI["PAGE_TITLE_PRINCIPAL"].SetText(Data[self.CurrentPage]["info"]["title"]["text"])
		for i in range(0, 5):
			self.GUI["PAGE_BONUSES_PRINCIPAL"][i].SetPackedFontColor(Data[self.CurrentPage]["info"]["bonus"]["color"])
			self.GUI["PAGE_BONUSES_PRINCIPAL"][i].SetText(Data[self.CurrentPage]["info"]["bonus"]["text%d" % (i + 1)])
		self.GUI["keystone"]["connector"].LoadImage(Data[self.CurrentPage]["connect"]["inactive"])
		self.GUI["keystone"]["title"].SetPackedFontColor(Data[self.CurrentPage]["info"]["title"]["color"])
		self.GUI["keystone"]["title"].SetText(localeInfo.RUNE_TEXT_75)
		self.GUI["keystone"]["title"].Show()
		self.GUI["keystone"]["text"].SetPackedFontColor(Data[self.CurrentPage]["info"]["bonus"]["color"])
		self.GUI["keystone"]["text"].SetText(localeInfo.RUNE_TEXT_76)
		self.GUI["keystone"]["text"].Show()
		self.GUI["keystone"]["icon"].Hide()
		for i in range(3):
			self.GUI["keystone"]["selection"][i].SetToolTipText(Runes[self.CurrentPage][i + 1]["bonus"])
			self.GUI["keystone"]["selection"][i].Hide()
			self.GUI["keystone"]["selection"][i].SetUpVisual(RUNE_DIR_PATH + "rune_page/rune_icons/%s/keystone%d.sub" % (Page_names[self.CurrentPage], i + 1))
			self.GUI["keystone"]["selection"][i].SetDownVisual(RUNE_DIR_PATH + "rune_page/rune_icons/%s/keystone%d.sub" % (Page_names[self.CurrentPage], i + 1))
			self.GUI["keystone"]["selection"][i].SetOverVisual(RUNE_DIR_PATH + "rune_page/rune_icons/%s/keystone%d.sub" % (Page_names[self.CurrentPage], i + 1))
		for i in range(3):
			self.GUI["runes"][i]["connector"].LoadImage(Data[self.CurrentPage]["connect"]["inactive"])
			self.GUI["runes"][i]["bg"].SetUpVisual(Data[self.CurrentPage]["circle"]["disabled"])
			self.GUI["runes"][i]["bg"].SetOverVisual(Data[self.CurrentPage]["circle"]["hover"])
			self.GUI["runes"][i]["bg"].SetDownVisual(Data[self.CurrentPage]["circle"]["active"])
			self.GUI["runes"][i]["icon"].LoadImage(RUNE_DIR_PATH + "rune_page/rune_icons/%s/keystone1.sub" % Page_names[self.CurrentPage])
			self.GUI["runes"][i]["icon"].Hide()
			self.GUI["runes"][i]["title"].SetPackedFontColor(Data[self.CurrentPage]["info"]["title"]["color"])
			self.GUI["runes"][i]["title"].SetText(localeInfo.RUNE_TEXT_77)
			self.GUI["runes"][i]["text"].SetPackedFontColor(Data[self.CurrentPage]["info"]["bonus"]["color"])
			self.GUI["runes"][i]["text"].SetText(localeInfo.RUNE_TEXT_78)
			for j in range(3):
				self.GUI["runes"][i]["selection"][j].Hide()
				self.GUI["runes"][i]["selection"][j].SetUpVisual(RUNE_DIR_PATH + "rune_page/rune_icons/%s/rune%d.sub" % (Page_names[self.CurrentPage], 3 * i  + j + 1))
				self.GUI["runes"][i]["selection"][j].SetDownVisual(RUNE_DIR_PATH + "rune_page/rune_icons/%s/rune%d.sub" % (Page_names[self.CurrentPage], 3 * i  + j + 1))
				self.GUI["runes"][i]["selection"][j].SetOverVisual(RUNE_DIR_PATH + "rune_page/rune_icons/%s/rune%d.sub" % (Page_names[self.CurrentPage], 3 * i  + j + 1))
				self.GUI["runes"][i]["selection"][j].SetToolTipText(Runes[self.CurrentPage][3 + 3 * i + j + 1]);
		
		for x in range(2):
			i = x + 3
			self.GUI["runes"][i]["connector"].LoadImage(Data[self.SecondaryPage]["connect"]["inactive"])
			self.GUI["runes"][i]["bg"].SetUpVisual(Data[self.SecondaryPage]["circle"]["disabled"])
			self.GUI["runes"][i]["bg"].SetOverVisual(Data[self.SecondaryPage]["circle"]["hover"])
			self.GUI["runes"][i]["bg"].SetDownVisual(Data[self.SecondaryPage]["circle"]["active"])
			self.GUI["runes"][i]["icon"].LoadImage(RUNE_DIR_PATH + "rune_page/rune_icons/%s/keystone1.sub" % Page_names[self.SecondaryPage])
			self.GUI["runes"][i]["icon"].Hide()
			self.GUI["runes"][i]["title"].SetPackedFontColor(Data[self.SecondaryPage]["info"]["title"]["color"])
			self.GUI["runes"][i]["title"].SetText(localeInfo.RUNE_TEXT_77)
			self.GUI["runes"][i]["text"].SetPackedFontColor(Data[self.SecondaryPage]["info"]["bonus"]["color"])
			self.GUI["runes"][i]["text"].SetText(localeInfo.RUNE_TEXT_78)
			for j in range(3):
				self.GUI["runes"][i]["selection"][j].Hide()
				self.GUI["runes"][i]["selection"][j].SetUpVisual(RUNE_DIR_PATH + "rune_page/rune_icons/%s/rune%d.sub" % (Page_names[self.SecondaryPage], 3 * x  + j + 1))
				self.GUI["runes"][i]["selection"][j].SetDownVisual(RUNE_DIR_PATH + "rune_page/rune_icons/%s/rune%d.sub" % (Page_names[self.SecondaryPage], 3 * x  + j + 1))
				self.GUI["runes"][i]["selection"][j].SetOverVisual(RUNE_DIR_PATH + "rune_page/rune_icons/%s/rune%d.sub" % (Page_names[self.SecondaryPage], 3 * x  + j + 1))
		
		self.GUI["PAGE_TITLE_SECONDARY"].SetPackedFontColor(Data[self.SecondaryPage]["info"]["title"]["color"])
		self.GUI["PAGE_TITLE_SECONDARY"].SetText(Data[self.SecondaryPage]["info"]["title"]["text"])
		for i in range(0, 2):
			self.GUI["PAGE_BONUSES_SECONDARY"][i].SetPackedFontColor(Data[self.SecondaryPage]["info"]["bonus"]["color"])
			self.GUI["PAGE_BONUSES_SECONDARY"][i].SetText(Data[self.SecondaryPage]["info"]["bonus"]["text%d" % (i + 1)])
		
		for i in range(5):
			self.GUI["PAGE_SET"][i].Enable()
			self.GUI["PAGE_SET"][i].SetSize(9, 9)
			self.GUI["PAGE_SET"][i].SetPosition(600 + 30 * i + 30, 570)
			
		self.GUI["PAGE_SET"][self.CurrentSet].Disable()
		self.GUI["PAGE_SET"][self.CurrentSet].SetSize(21, 21)
		self.GUI["PAGE_SET"][self.CurrentSet].SetPosition(600 + 30 * self.CurrentSet + 20, 565)
		if self.Keystone != 0:
			self.SelectKeystone(self.Keystone)
			
		for i in range(3):
			if self.GetRowStatus(i) == 0:
				self.GUI["runes"][i]["title"].SetPackedFontColor(Data[self.CurrentPage]["info"]["title"]["color"])
				self.GUI["runes"][i]["title"].SetText(localeInfo.RUNE_TEXT_77)
				self.GUI["runes"][i]["text"].SetPackedFontColor(Data[self.CurrentPage]["info"]["bonus"]["color"])
				self.GUI["runes"][i]["text"].SetText(localeInfo.RUNE_TEXT_78)
				self.GUI["runes"][i]["text"].Show()
				self.GUI["runes"][i]["title"].Show()
			else:
				if self.Runes[i] == 0:
					self.GUI["runes"][i]["title"].SetPackedFontColor(Data[self.CurrentPage]["info"]["title"]["color"])
					self.GUI["runes"][i]["title"].SetText(localeInfo.RUNE_TEXT_79)
					self.GUI["runes"][i]["text"].SetPackedFontColor(Data[self.CurrentPage]["info"]["bonus"]["color"])
					self.GUI["runes"][i]["text"].SetText(localeInfo.RUNE_TEXT_80)
					self.GUI["runes"][i]["text"].Show()
					self.GUI["runes"][i]["title"].Show()
				else:
					self.SelectRune(i, self.Runes[i])
					
		for x in range(2):
			i = x + 3
			if self.GetRowStatusSec(x) == 0:
				self.GUI["runes"][i]["title"].SetPackedFontColor(Data[self.SecondaryPage]["info"]["title"]["color"])
				self.GUI["runes"][i]["title"].SetText(localeInfo.RUNE_TEXT_77)
				self.GUI["runes"][i]["text"].SetPackedFontColor(Data[self.SecondaryPage]["info"]["bonus"]["color"])
				self.GUI["runes"][i]["text"].SetText(localeInfo.RUNE_TEXT_78)
				self.GUI["runes"][i]["text"].Show()
				self.GUI["runes"][i]["title"].Show()
			else:
				if self.Runes[i] == 0:
					self.GUI["runes"][i]["title"].SetPackedFontColor(Data[self.SecondaryPage]["info"]["title"]["color"])
					self.GUI["runes"][i]["title"].SetText(localeInfo.RUNE_TEXT_79)
					self.GUI["runes"][i]["text"].SetPackedFontColor(Data[self.SecondaryPage]["info"]["bonus"]["color"])
					self.GUI["runes"][i]["text"].SetText(localeInfo.RUNE_TEXT_80)
					self.GUI["runes"][i]["text"].Show()
					self.GUI["runes"][i]["title"].Show()
				else:
					self.SelectRuneSec(i, self.Runes[i])
		for i in range(3):
			self.GUI["seconadaries"][i].SetUp()
			self.GUI["seconadaries"][i].Enable()
			self.GUI["seconadaries"][i].SetDisableVisual(Data[i]["secondary"]["icon"]["active"])
		self.GUI["seconadaries"][self.SecondaryPage].Down()
		self.GUI["seconadaries"][self.SecondaryPage].Disable()
		self.GUI["seconadaries"][self.CurrentPage].SetDisableVisual(Data[self.CurrentPage]["secondary"]["icon"]["disabled"])
		self.GUI["seconadaries"][self.CurrentPage].Disable()
		
		for i in range(3):
			for j in range(3):
				self.GUI["runes"][i]["selection"][j].SetToolTipText(Runes[self.CurrentPage][(3*i) + j + 1 + 3]["bonus"])
		
		for x in range(2):
			i = x + 3
			for j in range(3):
				self.GUI["runes"][i]["selection"][j].SetToolTipText(Runes[self.SecondaryPage][(3*x) + j + 1 + 3]["bonus"])
				
		
		for j in range(3):
			self.GUI["runes"][4]["selection"][3 + j].SetUpVisual(RUNE_DIR_PATH + "rune_page/rune_icons/%s/rune%d.sub" % (Page_names[self.SecondaryPage], 3 * 2  + j + 1))
			self.GUI["runes"][4]["selection"][3 + j].SetDownVisual(RUNE_DIR_PATH + "rune_page/rune_icons/%s/rune%d.sub" % (Page_names[self.SecondaryPage], 3 * 2  +  j + 1))
			self.GUI["runes"][4]["selection"][3 + j].SetOverVisual(RUNE_DIR_PATH + "rune_page/rune_icons/%s/rune%d.sub" % (Page_names[self.SecondaryPage], 3 * 2  + j + 1))
			self.GUI["runes"][4]["selection"][3 + j].SetToolTipText(Runes[self.SecondaryPage][3 + 3 * 2 + j + 1]["bonus"])
			self.GUI["runes"][4]["selection"][3 + j].Hide()
				
	def Activate(self):
		text = "/activate_rune %d_%d_%d_%d_%d_%d_%d_%d_" % (self.CurrentPage, self.SecondaryPage, self.Keystone, self.Runes[0], self.Runes[1], self.Runes[2], self.Runes[3], self.Runes[4])
		net.SendChatPacket(text)

	def Delete(self):
		self.Reset()
		self.Configure()
	
	def Back(self):
		self.wndRunePrincipal.Board.Show()
		self.Hide()
	
	def Save(self):
		self.wndRunePrincipal.Parser.Set(CONFIG_SET  % (GetName(), self.CurrentSet), "page", self.CurrentPage)
		self.wndRunePrincipal.Parser.Set(CONFIG_SET  % (GetName(), self.CurrentSet), "keystone", self.Keystone)
		self.wndRunePrincipal.Parser.Set(CONFIG_SET  % (GetName(), self.CurrentSet), "secondary", self.SecondaryPage)
		self.wndRunePrincipal.Parser.Set(CONFIG_GLOBAL, "set", self.CurrentSet)
		for i in range(5):
			self.wndRunePrincipal.Parser.Set(CONFIG_SET % (GetName(), self.CurrentSet), "rune%d" % (i + 1), self.Runes[i])
		self.wndRunePrincipal.Parser.Save()
		self.Activate()
	
	def ClickKeystone(self):
		if self.GUI["keystone"]["title"].IsShow():
			self.GUI["keystone"]["title"].Hide()
			self.GUI["keystone"]["text"].Hide()
			for i in range(3):
				self.GUI["keystone"]["selection"][i].Show()
		else:
			self.GUI["keystone"]["title"].Show()
			self.GUI["keystone"]["text"].Show()
			for i in range(3):
				self.GUI["keystone"]["selection"][i].Hide()
	
	def SelectKeystone(self, key):
		if self.GetKeystoneStatus(key) == 1:
			self.Keystone = key
			for i in range(3):
				self.GUI["keystone"]["selection"][i].Hide()
			self.GUI["keystone"]["title"].Show()
			self.GUI["keystone"]["text"].Show()
			self.GUI["keystone"]["icon"].LoadImage(RUNE_DIR_PATH + "rune_page/rune_icons/%s/keystone%d.sub" % (Page_names[self.CurrentPage], key))
			self.GUI["keystone"]["icon"].Show()
			self.GUI["keystone"]["title"].SetPackedFontColor(Data[self.CurrentPage]["info"]["title"]["color"])
			self.GUI["keystone"]["title"].SetText(Runes[self.CurrentPage][key]["title"])
			self.GUI["keystone"]["text"].SetPackedFontColor(Data[self.CurrentPage]["info"]["bonus"]["color"])
			self.GUI["keystone"]["text"].SetText(Runes[self.CurrentPage][key]["bonus"])
			self.GUI["PAGE_BONUSES_PRINCIPAL"][0].SetText(Runes[self.CurrentPage][key]["bonus"])
			self.GUI["PAGE_BONUSES_PRINCIPAL"][0].SetPackedFontColor(Data[self.CurrentPage]["info"]["bonus"]["color"])
		
	def ClickRune(self, rune):
		if self.GUI["runes"][rune]["title"].IsShow():
			self.GUI["runes"][rune]["title"].Hide()
			self.GUI["runes"][rune]["text"].Hide()
			if rune == 4:
				for i in range(6):
					self.GUI["runes"][rune]["selection"][i].Show()
			else:
				for i in range(3):
					self.GUI["runes"][rune]["selection"][i].Show()
		else:
			self.GUI["runes"][rune]["title"].Show()
			self.GUI["runes"][rune]["text"].Show()
			if rune == 4:
				for i in range(6):
					self.GUI["runes"][rune]["selection"][i].Hide()
			else:
				for i in range(3):
					self.GUI["runes"][rune]["selection"][i].Hide()
	
	def GetKeystoneStatus(self, key):
		point = player.RUNE_PAGE1_KEYSTONE_START
		if self.CurrentPage == 1:
			point = player.RUNE_PAGE2_KEYSTONE_START
		elif self.CurrentPage == 2:
			point = player.RUNE_PAGE3_KEYSTONE_START
		
		return player.GetStatus(point + key - 1)
	
	def GetRowStatus(self, rune):
		point = player.RUNE_PAGE1_ROW_START
		if self.CurrentPage == 1:
			point = player.RUNE_PAGE2_ROW_START
		elif self.CurrentPage == 2:
			point = player.RUNE_PAGE3_ROW_START
		
		return player.GetStatus(point + rune)
		
	def GetRowStatusSec(self, rune):
		point = player.RUNE_PAGE1_ROW_START
		if self.SecondaryPage == 1:
			point = player.RUNE_PAGE2_ROW_START
		elif self.SecondaryPage == 2:
			point = player.RUNE_PAGE3_ROW_START
		
		return player.GetStatus(point + rune)

	def SelectRune(self, rune, selection):
		if self.GetRowStatus(rune) == 1:
			self.Runes[rune] = selection

			self.GUI["runes"][rune]["title"].Show()
			self.GUI["runes"][rune]["text"].Show()
			self.GUI["runes"][rune]["icon"].LoadImage(RUNE_DIR_PATH + "rune_page/rune_icons/%s/rune%d.sub" % (Page_names[self.CurrentPage], selection))
			self.GUI["runes"][rune]["icon"].Show()
			self.GUI["runes"][rune]["title"].SetPackedFontColor(Data[self.CurrentPage]["info"]["title"]["color"])
			self.GUI["runes"][rune]["title"].SetText(Runes[self.CurrentPage][3 + selection]["title"])
			self.GUI["runes"][rune]["text"].SetPackedFontColor(Data[self.CurrentPage]["info"]["bonus"]["color"])
			self.GUI["runes"][rune]["text"].SetText(Runes[self.CurrentPage][3 + selection]["bonus"])
			self.GUI["PAGE_BONUSES_PRINCIPAL"][rune + 1].SetText(Runes[self.CurrentPage][3 + selection]["bonus"])
			self.GUI["PAGE_BONUSES_PRINCIPAL"][rune + 1].SetPackedFontColor(Data[self.CurrentPage]["info"]["bonus"]["color"])
			for j in range(3):
				self.GUI["runes"][rune]["selection"][j].Hide()
				
	def SelectRuneSec(self, rune, selection):
		if self.GetRowStatusSec(rune - 3) == 1:
			self.Runes[rune] = selection
			self.GUI["runes"][rune]["title"].Show()
			self.GUI["runes"][rune]["text"].Show()
			self.GUI["runes"][rune]["icon"].LoadImage(RUNE_DIR_PATH + "rune_page/rune_icons/%s/rune%d.sub" % (Page_names[self.SecondaryPage], selection))
			self.GUI["runes"][rune]["icon"].Show()
			self.GUI["runes"][rune]["title"].SetPackedFontColor(Data[self.SecondaryPage]["info"]["title"]["color"])
			self.GUI["runes"][rune]["title"].SetText(Runes[self.SecondaryPage][3 + selection]["title"])
			self.GUI["runes"][rune]["text"].SetPackedFontColor(Data[self.SecondaryPage]["info"]["bonus"]["color"])
			self.GUI["runes"][rune]["text"].SetText(Runes[self.SecondaryPage][3 + selection]["bonus"])
			self.GUI["PAGE_BONUSES_SECONDARY"][rune - 3].SetText(Runes[self.SecondaryPage][3 + selection]["bonus"])
			self.GUI["PAGE_BONUSES_SECONDARY"][rune - 3].SetPackedFontColor(Data[self.SecondaryPage]["info"]["bonus"]["color"])
			for j in range(3):
				self.GUI["runes"][rune]["selection"][j].Hide()
			if rune == 4:
				for j in range(3):
					self.GUI["runes"][rune]["selection"][j + 3].Hide()
					
	def ActivateOnce(self):
		prg = self.wndRunePrincipal.Parser.Get(CONFIG_GLOBAL, "set", 0)
		crp = self.wndRunePrincipal.Parser.Get(CONFIG_SET  % (GetName(), prg), "page", 0)
		srp = self.wndRunePrincipal.Parser.Get(CONFIG_SET  % (GetName(), prg), "secondary", 1)
		krs = self.wndRunePrincipal.Parser.Get(CONFIG_SET  % (GetName(), prg), "keystone", 0)
		rns = [0,0,0,0,0,0]
		for i in range(5):
			rns[i] = self.wndRunePrincipal.Parser.Get(CONFIG_SET % (GetName(), prg), "rune%d" % (i + 1), 0)
		text = "/activate_rune %d_%d_%d_%d_%d_%d_%d_%d_" % (crp, srp, krs, rns[0], rns[1], rns[2], rns[3], rns[4])
		net.SendChatPacket(text)
	
	def OnPressEscapeKey(self):
		self.Hide()
		return True

class RuneSystem(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.Parser = RuneConfig()
		self.Pages = []
		self.wndRunePage = RunePage()
		self.wndRunePage.Bind(self)
		
		
		self.Board = ui.Board()
		self.Board.SetSize(813, 613)
		self.Board.SetCenterPosition()
		# self.Board.AddFlag("movable")
		# self.Board.AddFlag("float")
		self.Board.Hide()
		
		for i in range(3):
			self.Pages.append(ui.Button())
			self.Pages[i].SetParent(self.Board)
			self.Pages[i].SetSize(800, 200)
			self.Pages[i].SetPosition(5, 200 * i + 5)
			self.Pages[i].SetUpVisual(RUNE_DIR_PATH + "first_page/" + Page_names[i] + "/" + Page_names[i] + "01.tga")
			self.Pages[i].SetOverVisual(RUNE_DIR_PATH + "first_page/" + Page_names[i] + "/" + Page_names[i] + "02.tga")
			self.Pages[i].SetDownVisual(RUNE_DIR_PATH + "first_page/" + Page_names[i] + "/" + Page_names[i] + "03.tga")
			self.Pages[i].SetEvent(ui.mem_func(self.SelectPage), i)
			self.Pages[i].Show()
		
			
	def SelectPage(self, page):
		self.wndRunePage.SelectPage(page)
		self.Board.Hide()
		
	def __del__(self):
		ui.ScriptWindow.__del__(self)
	
	def Open(self):
		page = self.Parser.Get(CONFIG_GLOBAL, "set", 0)
		if self.wndRunePage.IsShow():
			self.wndRunePage.Hide()
		else:
			self.wndRunePage.Open(page)
	
	def Activate(self):
		if self.wndRunePage:
			self.wndRunePage.ActivateOnce()
	
	def Close(self):
		self.Board.Hide()
		self.wndRunePage.Hide()
		self.Hide()
