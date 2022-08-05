// Find //
#ifdef ENABLE_COSTUME_SYSTEM
	PyModule_AddIntConstant(poModule, "ENABLE_COSTUME_SYSTEM", 1);
#else
	PyModule_AddIntConstant(poModule, "ENABLE_COSTUME_SYSTEM", 0);
#endif

// Add After //
#ifdef ENABLE_RUNE_SYSTEM
	PyModule_AddIntConstant(poModule, "ENABLE_RUNE_SYSTEM", 1);
#else
	PyModule_AddIntConstant(poModule, "ENABLE_RUNE_SYSTEM", 0);
#endif