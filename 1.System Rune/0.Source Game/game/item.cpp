// Add //
#ifdef ENABLE_RUNE_SYSTEM
#include "new_rune_system.h"
#endif

// Find //
int CItem::FindEquipCell(LPCHARACTER ch, int iCandidateCell)
{
}

// Add After //
#ifdef ENABLE_RUNE_SYSTEM
void CItem::ModifyRunePoints(bool add)
{
	if(m_pOwner->HasRuneBonus(CRuneSystem::eBuffs::BUFF_STANDARD_EQUIPMENT))
	{
		if ((m_pProto->bType == ITEM_ARMOR))
		{
			long lDefGrade = m_pProto->alValues[1] + long(m_pProto->alValues[5] * 2);

			lDefGrade = ((lDefGrade * m_pOwner->GetBonusValue(CRuneSystem::eBuffs::BUFF_STANDARD_EQUIPMENT)) + 1) / 100;
			m_pOwner->ApplyPoint(APPLY_DEF_GRADE_BONUS, add ? lDefGrade : -lDefGrade);

			long lDefMagicBonus = m_pProto->alValues[0];
			lDefMagicBonus = ((lDefMagicBonus * m_pOwner->GetBonusValue(CRuneSystem::eBuffs::BUFF_STANDARD_EQUIPMENT)) + 1) / 100;

			m_pOwner->ApplyPoint(APPLY_MAGIC_DEF_GRADE, add ? lDefMagicBonus : -lDefMagicBonus);
			for (const auto& apply : m_pProto->aApplies)
			{
				if (apply.bType == APPLY_NONE)
					continue;

				if (apply.lValue <= 0)
					continue;

				long value = ((apply.lValue * m_pOwner->GetBonusValue(CRuneSystem::eBuffs::BUFF_STANDARD_EQUIPMENT)) + 1) / 100;

				m_pOwner->ApplyPoint(apply.bType, add ? value : -value);
			}
		}
		else if((m_pProto->bType == ITEM_WEAPON))
		{
			long lAttGrade = m_pProto->alValues[4] + m_pProto->alValues[5];
			if (m_pProto->alValues[3] > m_pProto->alValues[4])
			{
				lAttGrade = m_pProto->alValues[3] + m_pProto->alValues[5];
			}
			lAttGrade = ((lAttGrade * m_pOwner->GetBonusValue(CRuneSystem::eBuffs::BUFF_STANDARD_EQUIPMENT)) + 1) / 100;

			m_pOwner->ApplyPoint(APPLY_ATT_GRADE_BONUS, add ? lAttGrade : -lAttGrade);

			long lAttMagicGrade = m_pProto->alValues[2] + m_pProto->alValues[5];
			if (m_pProto->alValues[1] > m_pProto->alValues[2])
			{
				lAttMagicGrade = m_pProto->alValues[1] + m_pProto->alValues[5];
			}

			lAttMagicGrade = ((lAttMagicGrade * m_pOwner->GetBonusValue(CRuneSystem::eBuffs::BUFF_STANDARD_EQUIPMENT)) + 1) / 100;

			m_pOwner->ApplyPoint(APPLY_MAGIC_ATT_GRADE, add ? lAttMagicGrade : -lAttMagicGrade);
			for (const auto& apply : m_pProto->aApplies)
			{
				if (apply.bType == APPLY_NONE)
					continue;

				if (apply.lValue <= 0)
					continue;


				long value = ((apply.lValue * m_pOwner->GetBonusValue(CRuneSystem::eBuffs::BUFF_STANDARD_EQUIPMENT)) + 1) / 100;

				m_pOwner->ApplyPoint(apply.bType, add ? value : -value);
			}
		}
	}

	if(m_pOwner->HasRuneBonus(CRuneSystem::eBuffs::BUFF_COSTUME_BONUS))
	{
		if ((m_pProto->bType == ITEM_COSTUME))
		{
			for (const auto& apply : m_pProto->aApplies)
			{
				if (apply.bType == APPLY_NONE)
					continue;

				if (apply.lValue <= 0)
					continue;

				long value = ((apply.lValue * m_pOwner->GetBonusValue(CRuneSystem::eBuffs::BUFF_COSTUME_BONUS)) + 1) / 100;

				m_pOwner->ApplyPoint(apply.bType, add ? value : -value);
			}
			for (int i = 0; i < ITEM_ATTRIBUTE_MAX_NUM; ++i)
			{
				if (GetAttributeType(i))
				{
					const TPlayerItemAttribute& ia = GetAttribute(i);
					auto val = ia.sValue;
					val = ((val * m_pOwner->GetBonusValue(CRuneSystem::eBuffs::BUFF_COSTUME_BONUS)) + 1) / 100;
					if (ia.bType == APPLY_SKILL)
					{
						m_pOwner->ApplyPoint(ia.bType, add ? val : val ^ 0x00800000);
					}
					else
					{
						m_pOwner->ApplyPoint(ia.bType, add ? val : -val);
					}
				}
			}
		}
	}

	if(m_pOwner->HasRuneBonus(CRuneSystem::eBuffs::BUFF_PET_BONUS))
	{
		if ((m_pProto->bType == ITEM_PET && (m_pProto->bSubType == PET_SLOT)))
		{
			if(m_pProto->bSubType == PET_SLOT)
			{
				for (int i = 0; i < ITEM_ATTRIBUTE_MAX_NUM; ++i)
				{
					if (GetAttributeType(i))
					{
						const TPlayerItemAttribute& ia = GetAttribute(i);
						auto val = ia.sValue;

						val = ((val * m_pOwner->GetBonusValue(CRuneSystem::eBuffs::BUFF_PET_BONUS)) + 1) / 100;
						if (ia.bType == APPLY_SKILL)
						{
							m_pOwner->ApplyPoint(ia.bType, add ? val : val ^ 0x00800000);
						}
						else
						{
							m_pOwner->ApplyPoint(ia.bType, add ? val : -val);
						}
					}
				}
			}
			else
			{
				for (int i = 0; i < ITEM_ATTRIBUTE_MAX_NUM; ++i)
				{
					if (GetAttributeType(i))
					{
						const TPlayerItemAttribute& ia = GetAttribute(i);
						auto val = ia.sValue;
						val = ((val * m_pOwner->GetBonusValue(CRuneSystem::eBuffs::BUFF_PET_BONUS)) + 1) / 100;
						if (ia.bType == APPLY_SKILL)
						{
							m_pOwner->ApplyPoint(ia.bType, add ? val : val ^ 0x00800000);
						}
						else
						{
							m_pOwner->ApplyPoint(ia.bType, add ? val : -val);
						}
					}
				}
			}
			for (const auto& apply : m_pProto->aApplies)
			{
				if (apply.bType == APPLY_NONE)
					continue;

				if (apply.lValue <= 0)
					continue;

				long value = ((apply.lValue * m_pOwner->GetBonusValue(CRuneSystem::eBuffs::BUFF_PET_BONUS)) + 1) / 100;

				m_pOwner->ApplyPoint(apply.bType, add ? value : -value);
			}
		}
	}

	if(m_pOwner->HasRuneBonus(CRuneSystem::eBuffs::BUFF_MOUNT_BONUS))
	{
		if ((m_pProto->bType == ITEM_COSTUME && (m_pProto->bSubType == COSTUME_MOUNT)))
		{
			for (const auto& apply : m_pProto->aApplies)
			{
				if (apply.bType == APPLY_NONE)
					continue;

				if (apply.lValue <= 0)
					continue;

				long value = ((apply.lValue * m_pOwner->GetBonusValue(CRuneSystem::eBuffs::BUFF_MOUNT_BONUS)) + 1) / 100;

				m_pOwner->ApplyPoint(apply.bType, add ? value : -value);
			}
			for (int i = 0; i < ITEM_ATTRIBUTE_MAX_NUM; ++i)
			{
				if (GetAttributeType(i))
				{
					const TPlayerItemAttribute& ia = GetAttribute(i);
					auto val = ia.sValue;
					val = ((val * m_pOwner->GetBonusValue(CRuneSystem::eBuffs::BUFF_MOUNT_BONUS)) + 1) / 100;
					if (ia.bType == APPLY_SKILL)
					{
						m_pOwner->ApplyPoint(ia.bType, add ? val : val ^ 0x00800000);
					}
					else
					{
						m_pOwner->ApplyPoint(ia.bType, add ? val : -val);
					}
				}
			}
		}
	}

	if(m_pOwner->HasRuneBonus(CRuneSystem::eBuffs::BUFF_MORE_POTIONS))
	{
		if ((m_pProto->bType == ITEM_USE && (m_pProto->bSubType == USE_AFFECT)))
		{
			for (const auto& apply : m_pProto->aApplies)
			{
				if (apply.bType == APPLY_NONE)
					continue;

				if (apply.lValue <= 0)
					continue;

				long value = ((apply.lValue * m_pOwner->GetBonusValue(CRuneSystem::eBuffs::BUFF_MORE_POTIONS)) + 1) / 100;

				m_pOwner->ApplyPoint(apply.bType, add ? value : -value);
			}
			for (int i = 0; i < ITEM_ATTRIBUTE_MAX_NUM; ++i)
			{
				if (GetAttributeType(i))
				{
					const TPlayerItemAttribute& ia = GetAttribute(i);
					auto val = ia.sValue;
					val = ((val * m_pOwner->GetBonusValue(CRuneSystem::eBuffs::BUFF_MORE_POTIONS)) + 1) / 100;
					if (ia.bType == APPLY_SKILL)
					{
						m_pOwner->ApplyPoint(ia.bType, add ? val : val ^ 0x00800000);
					}
					else
					{
						m_pOwner->ApplyPoint(ia.bType, add ? val : -val);
					}
				}
			}
		}
	}
}
#endif

// Find //
	ModifyRunePoints(bAdd);

// Replace //
#ifdef ENABLE_RUNE_SYSTEM
#ifdef ENABLE_FAKE_PC
	if (pkChr && !pkChr->FakePC_Check())
	{
		ModifyRunePoints(bAdd);
	}
#else
	ModifyRunePoints(bAdd);
#endif
#endif