// Find //
ACMD(do_rewarp);

// Add After //
#ifdef ENABLE_RUNE_SYSTEM
ACMD(do_activate_rune);
#endif

// Find //
	{ "rewarp", do_rewarp, 0, POS_DEAD, GM_HIGH_WIZARD },

// Add After //
#ifdef ENABLE_RUNE_SYSTEM
	{ "activate_rune", do_activate_rune, 0, POS_DEAD, GM_PLAYER },
#endif