// Add //
#ifdef ENABLE_RUNE_SYSTEM
#include "new_rune_system.h"
#endif

// Find //
	float k = (float) ch->GetSkillPowerByLevel( MIN((int)SKILL_MAX_LEVEL, m_iLeadership ) )/ 100.0f;

// Add After //
#ifdef ENABLE_RUNE_SYSTEM
	if (GetLeaderCharacter())
	{
		if(GetLeaderCharacter()->HasRuneBonus(CRuneSystem::eBuffs::BUFF_LEADER_BONUS))
		{
			k += (float)(k * GetLeaderCharacter()->GetBonusValue(CRuneSystem::eBuffs::BUFF_LEADER_BONUS)) / 100.0f;
		}
	}
#endif