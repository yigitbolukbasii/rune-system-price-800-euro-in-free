// Add //
#ifdef ENABLE_RUNE_SYSTEM
#include "new_rune_system.h"
#endif

// Find //
	if (GetWear(WEAR_WEAPON) && (GetWear(WEAR_WEAPON)->GetType() == ITEM_ROD || GetWear(WEAR_WEAPON)->GetType() == ITEM_PICK))
	{
		return false;
	}

// Add After //
#ifdef ENABLE_RUNE_SYSTEM
	if(HasRuneBonus(CRuneSystem::eBuffs::BUFF_COOLDOWN_RESET))
	{
		SetPoint(POINT_CASTING_SPEED, 0);
		ComputePoints();
		int chance = number(1, 100);
		if(chance >= 100 - GetBonusValue(CRuneSystem::eBuffs::BUFF_COOLDOWN_RESET))
		{
			PointChange(POINT_CASTING_SPEED, 10000);
		}
	}
#endif