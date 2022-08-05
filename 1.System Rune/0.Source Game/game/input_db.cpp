// Add //
#ifdef ENABLE_RUNE_SYSTEM
#include "new_rune_system.h"
#endif

// Find //
	CBuildingManager::instance().FinalizeBoot();
	CMotionManager::instance().Build();

// Add After //
#ifdef ENABLE_RUNE_SYSTEM
	CRuneSystem::instance().LoadRunes();
#endif