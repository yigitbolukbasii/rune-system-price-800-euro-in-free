// Find //
import locale

// Add After //
if app.ENABLE_RUNE_SYSTEM:
	import uiRune

// Find //
		self.__SetQuickSlotMode()
		self.__ServerCommand_Build()
		self.__ProcessPreservedServerCommand()

// Add After //
		if app.ENABLE_RUNE_SYSTEM:
			self.uiRuneSystem = uiRune.RuneSystem()
			self.uiRuneSystem.Hide()

// Find //
		try:
			self.StartGame()
		except:
			exception.Abort("GameWindow.Open")

// Add After //
		if app.ENABLE_RUNE_SYSTEM:
			if self.uiRuneSystem:
				self.uiRuneSystem.Activate()

// Find //
	def __ClickOKey(self):
		if app.IsPressed(app.DIK_LCONTROL) or app.IsPressed(app.DIK_RCONTROL):
			self.interface.DragonSoulActivateByKey()
		else:
			self.interface.ToggleDragonSoulWindowWithNoInfo()

// Find //
		if app.ENABLE_RUNE_SYSTEM:
			if self.uiRuneSystem:
				self.uiRuneSystem.Activate()

// Add Before //
	if app.ENABLE_RUNE_SYSTEM:
		def __OpenRuneGUI(self):
			self.uiRuneSystem.Open()

		def RefreshRune(self):
			if self.uiRuneSystem:
				self.uiRuneSystem.Refresh()

// Find //
		if self.targetBoard:
			self.targetBoard.Destroy()
			self.targetBoard = None

// Add Before //
		if app.ENABLE_RUNE_SYSTEM:
			if self.uiRuneSystem:
				self.uiRuneSystem.Close()
				self.uiRuneSystem = None

// Find //
		self.interface.BUILD_OnUpdate()

// Add Aftar //
		if app.ENABLE_RUNE_SYSTEM:
			if constInfo.RUNE_SYSTEM==1:
				constInfo.RUNE_SYSTEM = 0
				self.__OpenRuneGUI()


// Find //
	def __ServerCommand_Build(self):
{
}

// Add Aftar //
		if app.ENABLE_RUNE_SYSTEM:
			serverCommandList["rune_refresh"] = self.RefreshRune
