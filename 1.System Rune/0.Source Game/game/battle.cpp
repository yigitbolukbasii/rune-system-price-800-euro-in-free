// Add //
#ifdef ENABLE_RUNE_SYSTEM
#include "new_rune_system.h"
#endif

// Find //
	iRetDam = iDam;

// Add After //
#ifdef ENABLE_RUNE_SYSTEM
	if(pkAttacker)
	{
		if(pkAttacker->HasRuneBonus(CRuneSystem::eBuffs::BUFF_TRUE_DAMAGE) || pkAttacker->HasRuneBonus(CRuneSystem::eBuffs::BUFF_BLOCK_DESTROY))
		{
			pkAttacker->RegisterStrike((DWORD)pkVictim->GetVID());
		}

		if(pkAttacker->HasRuneBonus(CRuneSystem::eBuffs::BUFF_TRUE_DAMAGE) && pkAttacker->IsPC() && pkVictim->IsPC() == false)
		{
			DWORD iStrikesCount = 0;
			if(pkAttacker->GetStrikeByVid((DWORD)pkVictim->GetVID(), &iStrikesCount))
			{
				if(iStrikesCount >= 3)
				{
					pkVictim->PointChange(POINT_HP, -1000);
					pkVictim->SendDamagePacket(pkAttacker, 1000, CRuneSystem::eDamageFlag::DAMAGE_PENETRATE);
					pkAttacker->ResetStrikes((DWORD)pkVictim->GetVID());
				}
			}
		}
	}
#endif