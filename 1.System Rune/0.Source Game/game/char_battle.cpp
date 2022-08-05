// Add //
#ifdef ENABLE_RUNE_SYSTEM
#include "new_rune_system.h"
#endif

// Find //
	if (ITEM_MANAGER::instance().CreateDropItem(this, pkAttacker, s_vec_item))
	{
		if (s_vec_item.empty())
		{
		}
		else if (s_vec_item.size() == 1)
		{
			item = s_vec_item[0];
			item->AddToGround(GetMapIndex(), pos);

			if (!CBattleArena::instance().IsBattleArenaMap(pkAttacker->GetMapIndex()))
			{
				item->SetOwnership(pkAttacker);
			}
			item->StartDestroyEvent();
			pos.x = number(-7, 7) * 20;
			pos.y = number(-7, 7) * 20;
			pos.x += GetX();
			pos.y += GetY();

// Add After //
#ifdef ENABLE_RUNE_SYSTEM
			if(GetMobRank() >= MOB_RANK_BOSS)
			{
				if(pkAttacker->HasRuneBonus(CRuneSystem::eBuffs::BUFF_DROP_BOSS))
				{
					int chance = pkAttacker->GetBonusValue(CRuneSystem::eBuffs::BUFF_DROP_BOSS);
					if(number(1, 100) > 100 - chance)
					{
						LPITEM rune_bonus = ITEM_MANAGER::instance().CreateItem(item->GetVnum(), 1, 0, false);
						if(rune_bonus)
						{
							rune_bonus->AddToGround(GetMapIndex(), pos);
							rune_bonus->AddToGround(GetMapIndex(), pos);
							rune_bonus->SetOwnership(pkAttacker);
							rune_bonus->StartDestroyEvent();
						}
					}
				}
			}
#endif

// Find //
			std::vector<LPCHARACTER> v;

// Add After //
#ifdef ENABLE_RUNE_SYSTEM
			std::vector<DWORD> Gotten;
#endif

// Find //
					if (!CBattleArena::instance().IsBattleArenaMap(ch->GetMapIndex()))
					{
						item->SetOwnership(ch);
					}
					item->StartDestroyEvent();
					pos.x = number(-7, 7) * 20;
					pos.y = number(-7, 7) * 20;
					pos.x += GetX();
					pos.y += GetY();

// Add After //
#ifdef ENABLE_RUNE_SYSTEM
					if(GetMobRank() >= MOB_RANK_BOSS)
					{
						if(ch->HasRuneBonus(CRuneSystem::eBuffs::BUFF_DROP_BOSS) && std::find(Gotten.begin(), Gotten.end(), ch->GetVID()) == Gotten.end())
						{
							int chance = ch->GetBonusValue(CRuneSystem::eBuffs::BUFF_DROP_BOSS);
							if(number(1, 100) > 100 - chance)
							{
								LPITEM rune_bonus = ITEM_MANAGER::instance().CreateItem(item->GetVnum(), 1, 0, false);
								if(rune_bonus)
								{
									rune_bonus->AddToGround(GetMapIndex(), pos);
									rune_bonus->AddToGround(GetMapIndex(), pos);
									rune_bonus->SetOwnership(ch);
									rune_bonus->StartDestroyEvent();
									Gotten.push_back(ch->GetVID());
								}
							}
						}
					}
#endif

// Find //
					sys_log(0, "DROP_ITEM: %s %d %d by %s", item->GetName(), pos.x, pos.y, GetName());
				}
			}

// Add After //
#ifdef ENABLE_RUNE_SYSTEM
			Gotten.clear();
#endif

// Find //
	if (true == IsMonster() && 2493 == GetMobTable().dwVnum)
	{
		if (NULL != pkKiller && NULL != pkKiller->GetGuild())
		{
			CDragonLairManager::instance().OnDragonDead(this, pkKiller->GetGuild()->GetID());
		}
		else
		{
			sys_err("DragonLair: Dragon killed by nobody");
		}
	}

// Add After //
#ifdef ENABLE_RUNE_SYSTEM
	if(pkKiller && pkKiller->IsPC() && IsPC() && pkKiller->IsDead() == false)
	{
		if(pkKiller->HasRuneBonus(CRuneSystem::eBuffs::BUFF_RESTORE_HEALTH))
		{
			pkKiller->SetHP(std::min(pkKiller->GetMaxHP(), pkKiller->GetHP() + (pkKiller->GetMaxHP() * 50 / 100)));
		}
	}
	if(pkKiller && pkKiller->IsPC() && IsNPC() && GetMobRank() >= 4)
	{
		if(pkKiller->HasRuneBonus(CRuneSystem::eBuffs::BUFF_ATTACK))
		{
			pkKiller->SetQuestFlag("rune_system.bosses", pkKiller->GetQuestFlag("rune_system.bosses"));
			pkKiller->AddAffect(AFFECT_RUNE, APPLY_MALL_ATTBONUS, 10, 0, 3600 * 60 * 60, 0, true, true);
		}
	}
#endif

// Find //
	else if (type == DAMAGE_TYPE_NORMAL || type == DAMAGE_TYPE_NORMAL_RANGE)
	{

// Add After //
#ifdef ENABLE_RUNE_SYSTEM
		bool bMissNow = false;
		if(pAttacker && pAttacker->HasRuneBonus(CRuneSystem::eBuffs::BUFF_BLOCK_DESTROY) && pAttacker->IsPC() && IsPC())
		{
			DWORD iStrikesCount = 0;
			if(pAttacker->GetStrikeByVid((DWORD)GetVID(), &iStrikesCount))
			{
				if(iStrikesCount >= 5)
				{
					bMissNow = true;
					pAttacker->ResetStrikes((DWORD)GetVID());
				}
			}
		}
		if(bMissNow == false)
	{
#endif

// Find //
		if (IsAffectFlag(AFF_JEONGWIHON))
		{
			SET_BIT(damageEventsFlag, EDamageEvents::BERSEK);
			dam = (int)(dam * (100 + GetSkillPower(SKILL_JEONGWI) * 25 / 100) / 100);
		}

// Add After //
#ifdef ENABLE_RUNE_SYSTEM
	}
#endif

// Find //
	if (type == DAMAGE_TYPE_POISON)
	{
		if (GetHP() - dam <= 0)
		{
			dam = GetHP() - 1;
		}
	}

// Add After //
#ifdef ENABLE_RUNE_SYSTEM
	if(pAttacker && pAttacker->HasRuneBonus(CRuneSystem::eBuffs::BUFF_CRIT_DAMAGE))
	{
		if(IsCritical)
		{
			dam += pAttacker->GetBonusValue(CRuneSystem::eBuffs::BUFF_CRIT_DAMAGE) * dam / 100;
		}
	}
#endif
