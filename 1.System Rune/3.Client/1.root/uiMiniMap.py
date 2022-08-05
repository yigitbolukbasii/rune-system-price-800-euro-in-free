// Find //
		self.serverInf = None

// Add Aftar //
		if app.ENABLE_RUNE_SYSTEM:
			self.btnRune = 0

// Find //
		self.serverInfo=self.GetChild("ServerInfo")

// Add Aftar //
			if app.ENABLE_RUNE_SYSTEM:
				self.btnRune = self.GetChild("Rune")

// Find //
		self.MiniMapShowButton.SetEvent(ui.mem_func(self.ShowMiniMap))

// Add Aftar //
		if app.ENABLE_RUNE_SYSTEM:
			self.btnRune.SetEvent(ui.mem_func(self.RuneWindow))

// Find //
	def ToggleAtlasWindow(self):
		if not miniMap.IsAtlas():
			return
		if self.AtlasWindow.IsShow():
			self.AtlasWindow.Hide()
		else:
			self.AtlasWindow.Show()

// Add Aftar //
	if app.ENABLE_RUNE_SYSTEM:
		def RuneWindow(self):
			constInfo.RUNE_SYSTEM = 1