// Add //
#ifdef ENABLE_RUNE_SYSTEM
#include "new_rune_system.h"
#endif

// Find //
	while (it != m_list_pkAffect.end())
	{
		CAffect* pkAff = *it;

		if (bSave)
		{
			if (IS_NO_CLEAR_ON_DEATH_AFFECT(pkAff->dwType) || IS_NO_SAVE_AFFECT(pkAff->dwType))
			{
				++it;
				continue;
			}

// Add After //
#ifdef ENABLE_RUNE_SYSTEM
			if(pkAff->dwType == AFFECT_RUNE)
			{
				++it;
				continue;
			}
#endif

// Find //
	if (lDuration == 0)
	{
		sys_err("Character::AddAffect lDuration == 0 type %d", lDuration, dwType);
		lDuration = 1;
	}

// Add After //
#ifdef ENABLE_RUNE_SYSTEM
	switch (dwType)
	{
		case SKILL_HOSIN:
		case SKILL_REFLECT:
		case SKILL_GICHEON:
		case SKILL_JEONGEOP:
		case SKILL_KWAESOK:
		case SKILL_JEUNGRYEOK:
		case SKILL_JEONGWI:
		case SKILL_GEOMKYUNG:
		case SKILL_CHUNKEON:
		case SKILL_GWIGEOM:
		case SKILL_TERROR:
		case SKILL_JUMAGAP:
		case SKILL_MANASHIELD:
		case SKILL_GYEONGGONG:
		case SKILL_EUNHYUNG:
		{
			if(HasRuneBonus(CRuneSystem::eBuffs::BUFF_HALF_DAY))
			{
				lDuration += 3600 * 12;
			}
			if(HasRuneBonus(CRuneSystem::eBuffs::BUFF_STRONGER))
			{
				lApplyValue += GetBonusValue(CRuneSystem::eBuffs::BUFF_STRONGER);
			}
		}
		break;
		default:
			break;
}
#endif
