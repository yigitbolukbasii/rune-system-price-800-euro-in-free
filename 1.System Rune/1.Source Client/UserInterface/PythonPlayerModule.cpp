// Find //
	PyModule_AddIntConstant(poModule, "GROUND", GROUND);

// Add After //
#ifdef ENABLE_RUNE_SYSTEM
	PyModule_AddIntConstant(poModule, "RUNE_PAGE1_KEYSTONE_START", POINT_RUNE_PAGE1_KEYSTONE1);
	PyModule_AddIntConstant(poModule, "RUNE_PAGE2_KEYSTONE_START", POINT_RUNE_PAGE2_KEYSTONE1);
	PyModule_AddIntConstant(poModule, "RUNE_PAGE3_KEYSTONE_START", POINT_RUNE_PAGE3_KEYSTONE1);
	PyModule_AddIntConstant(poModule, "RUNE_PAGE1_ROW_START", POINT_RUNE_PAGE1_ROW1);
	PyModule_AddIntConstant(poModule, "RUNE_PAGE2_ROW_START", POINT_RUNE_PAGE2_ROW1);
	PyModule_AddIntConstant(poModule, "RUNE_PAGE3_ROW_START", POINT_RUNE_PAGE3_ROW1);
#endif