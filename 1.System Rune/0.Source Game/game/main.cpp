// Add //
#ifdef ENABLE_RUNE_SYSTEM
#include "new_rune_system.h"
#endif

// Find //
	if (!start(argc, argv))
	{
		return 0;
	}
// Add After //
#ifdef ENABLE_RUNE_SYSTEM
	CRuneSystem runeSystem;
#endif