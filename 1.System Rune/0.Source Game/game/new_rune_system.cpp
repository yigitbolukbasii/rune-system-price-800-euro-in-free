#include "stdafx.h"
#ifdef ENABLE_RUNE_SYSTEM
#include "utils.h"
#include "vector.h"
#include "char.h"
#include "sectree_manager.h"
#include "char_manager.h"
#include "mob_manager.h"
#include "new_rune_system.h"
#include "packet.h"
#include "item_manager.h"
#include "item.h"
#include "text_file_loader.h"
#include "group_text_parse_tree.h"
#include "locale_service.h"
#include "locale.h"
#include "affect.h"

CRuneSystem::CRuneSystem()
{
	for(auto r : Runes)
	{
		r.clear();
	}
}

CRuneSystem::~CRuneSystem() {}

void CRuneSystem::LoadRunes()
{
	char szTitleTableFileName[256];
	snprintf(szTitleTableFileName, sizeof(szTitleTableFileName), "%s/quest/files/txt/rune_config.txt", LocaleService_GetBasePath().c_str());
	CTextFileLoader loader;

	if (!loader.Load(szTitleTableFileName))
	{
		return;
	}

	std::string stName;

	for (DWORD i = 0; i < loader.GetChildNodeCount(); ++i)
	{
		loader.SetChildNode(i);
		loader.GetCurrentNodeName(&stName);
		int iRune = 0;
		int iRunePage = 0;
		int iRuneCost = 0;
		std::map<DWORD, int> items;
		std::map<DWORD, int> bonuses;

		if (!loader.GetTokenInteger("rune", &iRune))
		{
			sys_err("CRuneSystem::LoadRunes : Syntax error {} : no rune id, node {}", szTitleTableFileName, stName.c_str());
			loader.SetParentNode();
			return;
		}

		if (!loader.GetTokenInteger("page", &iRunePage))
		{
			sys_err("CRuneSystem::LoadRunes : Syntax error {} : no rune page, node {}", szTitleTableFileName, stName.c_str());
			loader.SetParentNode();
			return;
		}

		if (!loader.GetTokenInteger("cost", &iRuneCost))
		{
			sys_err("CRuneSystem::LoadRunes : Syntax error {} : no rune cost, node {}", szTitleTableFileName, stName.c_str());
			loader.SetParentNode();
			return;
		}

		TTokenVector * pTok;

		for(int k = 1; k < 10; ++k)
		{
			char buf[25];
			snprintf(buf, sizeof(buf), "require_item%d", k);
			if (loader.GetTokenVector(buf, &pTok))
			{
				if(pTok->size() >= 2)
				{	
					items.insert(std::make_pair(atoi(pTok->at(0).c_str()), atoi(pTok->at(1).c_str())));
				}
				else
				{
					sys_err("CRuneSystem::LoadRunes : Syntax error {} : incorrect required_item, node {}", szTitleTableFileName, stName.c_str());
					loader.SetParentNode();
					return;
				}
				continue;
			}
			break;
		}

		for(int k = 1; k < 10; ++k)
		{
			char buf[10];
			snprintf(buf, sizeof(buf), "bonus%d", k);
			if (loader.GetTokenVector(buf, &pTok))
			{
				if(pTok->size() >= 2)
				{
					bonuses.insert(std::make_pair(atoi(pTok->at(0).c_str()), atoi(pTok->at(1).c_str())));
				}
				else
				{
					sys_err("CRuneSystem::LoadRunes : Syntax error {} : incorrect bonus, node {}", szTitleTableFileName, stName.c_str());
					loader.SetParentNode();
					return;
				}
				continue;
			}
			break;
		}

		Rune_struct Rune;
		Rune.runeID = iRune;
		Rune.costValue = iRuneCost;
		Rune.items = items;
		Rune.bonuses = bonuses;
		Runes[iRunePage].push_back(Rune);
		loader.SetParentNode();
	}
}

CRuneSystem::Rune_struct CRuneSystem::GetRuneInfo(int page, int runeID)
{
	Rune_struct ret;
	if(page < 3 && page >= 0)
	{
		for(size_t i = 0; i < Runes[page].size(); ++i)
		{
			if(Runes[page][i].runeID == runeID)
			{
				ret = Runes[page][i];
			}
		}
	}
	return ret;
}

bool CRuneSystem::GrantRune(LPCHARACTER ch, int page, int row)
{
	if(!ch)
	{
		return false;
	}
	
	if(page > 2 || page < 0)
	{
		return false;
	}
	
	if(row > 3 || row < 0)
	{
		return false;
	}
	
	int point_start = POINT_RUNE_PAGE1_ROW1, point_check = POINT_RUNE_PAGE1_KEYSTONE1;

	if(page == 1)
	{
		point_start = POINT_RUNE_PAGE2_ROW1;
		point_check = POINT_RUNE_PAGE2_KEYSTONE1;
	}
	else if(page == 2)
	{
		point_start = POINT_RUNE_PAGE3_ROW1;
		point_check = POINT_RUNE_PAGE3_KEYSTONE1;
	}

	if(row == 1)
	{
		bool can_continue = false;

		for(int i = 0; i < 3; i++)
		{
			if(ch->GetPoint(point_check + i) == 1)
			{
				can_continue = true;
				break;
			}
		}

		if(!can_continue)
		{
			ch->ChatInfoTrans(("RUNE_AT_LEAST_ONE_KEYSTONE_MUST_BE_ENABLED"));
			return false;
		}

		Rune_struct rn = GetRuneInfo(page, row + 3);

		if(ch->GetGold() < rn.costValue)
		{
			ch->ChatInfoTrans(("RUNE_YOU_DO_NOT_HAVE_ENOUGH_MONEY_FOR_RUNE"));
			return false;
		}

		for(auto item : rn.items)
		{
			if(ch->CountSpecifyItem(item.first) < item.second)
			{
				LPITEM name_item = ITEM_MANAGER::instance().CreateItem(item.first, 1, 0, false);
				if(name_item)
				{
					ch->ChatInfoTrans(("RUNE_YOU_NEED_%d_X_%s_IN_ORDER_TO_DO_THIS"), item.second, name_item->GetName());
				}
				else
				{
					ch->ChatInfoTrans(("RUNE_YOU_DO_NOT_HAVE_ENOUGH_ITEMS"));
				}
				M2_DESTROY_ITEM(name_item);
				return false;
			}
		}

		for(auto item : rn.items)
		{
			ch->RemoveSpecifyItem(item.first, item.second);
		}

		ch->ChangeGold(-rn.costValue);
		ch->PointChange(point_start, 1);
		ch->UpdatePacket();
		ch->ChatInfoTrans(("RUNE_YOU_ROW_SUCCESSFULLY_UNLOCKED"));
	}
	else
	{
		if(row == 2)
		{
			point_check = point_start;
		}
		else
		{
			point_check = point_start + 1;
		}

		if(ch->GetPoint(point_check) != 1)
		{
			ch->ChatInfoTrans(("RUNE_YOU_MUST_UNLOCK_THE_RUNE_ROWS_IN_ASCENDING_ORDER"));
			return false;
		}

		Rune_struct rn = GetRuneInfo(page, row + 3);

		if(ch->GetGold() < rn.costValue)
		{
			ch->ChatInfoTrans(("RUNE_YOU_DO_NOT_HAVE_ENOUGH_MONEY_FOR_RUNE"));
			return false;
		}

		for(auto item : rn.items)
		{
			if(ch->CountSpecifyItem(item.first) < item.second)
			{
				LPITEM name_item = ITEM_MANAGER::instance().CreateItem(item.first, 1, 0, false);
				if(name_item)
				{
					ch->ChatInfoTrans(("RUNE_YOU_NEED_%d_X_%s_IN_ORDER_TO_DO_THIS"), item.second, name_item->GetName());
				}
				else
				{
					ch->ChatInfoTrans(("RUNE_YOU_DO_NOT_HAVE_ENOUGH_ITEMS"));
				}
				M2_DESTROY_ITEM(name_item);
				return false;
			}
		}

		for(auto item : rn.items)
		{
			ch->RemoveSpecifyItem(item.first, item.second);
		}

		long long gold = static_cast<long long>(rn.costValue);
		ch->ChangeGold(-gold);
		ch->PointChange(point_start + row - 1, 1);
		ch->UpdatePacket();
		ch->ChatInfoTrans(("RUNE_YOU_ROW_SUCCESSFULLY_UNLOCKED"));
	}
	return true;
}

bool CRuneSystem::GrantKeystone(LPCHARACTER ch, int page, int keystone)
{
	if(!ch)
	{
		return false;
	}
	
	if(page > 2 || page < 0)
	{
		return false;
	}
	
	if(keystone > 3 || keystone < 0)
	{
		return false;
	}
	
	int point_start = POINT_RUNE_PAGE1_KEYSTONE1;

	if(page == 1)
	{
		point_start = POINT_RUNE_PAGE2_KEYSTONE1;
	}
	else if(page == 2)
	{
		point_start = POINT_RUNE_PAGE3_KEYSTONE1;
	}
	
	Rune_struct rn = GetRuneInfo(page, keystone);

	if(ch->GetGold() < rn.costValue)
	{
		ch->ChatInfoTrans(("RUNE_YOU_DO_NOT_HAVE_ENOUGH_MONEY_FOR_KEYSTONE"));
		return false;
	}

	for(auto item : rn.items)
	{
		if(ch->CountSpecifyItem(item.first) < item.second)
		{
			LPITEM name_item = ITEM_MANAGER::instance().CreateItem(item.first, 1, 0, false);
			if(name_item)
			{
				ch->ChatInfoTrans(("RUNE_YOU_NEED_%d_X_%s_IN_ORDER_TO_DO_THIS"), item.second, name_item->GetName());
			}
			else
			{
				ch->ChatInfoTrans(("RUNE_YOU_DO_NOT_HAVE_ENOUGH_ITEMS"));
			}
			M2_DESTROY_ITEM(name_item);
			return false;
		}
	}

	for(auto item : rn.items)
	{
		ch->RemoveSpecifyItem(item.first, item.second);
	}

	long long gold = static_cast<long long>(rn.costValue);
	ch->ChangeGold(-rn.costValue);
	ch->PointChange(point_start + keystone - 1, 1);
	ch->UpdatePacket();
	ch->ChatInfoTrans(("RUNE_YOU_KEYSTONE_SUCCESSFULLY_UNLOCKED"));
	return true;
}

void CRuneSystem::ActivateBonus(LPCHARACTER ch, int page, int sec_page, int keystone, std::string set)
{
	if(!ch)
	{
		return;
	}
	
	if(page > 2 || page < 0)
	{
		return;
	}
	
	if(sec_page > 2 || sec_page < 0)
	{
		return;
	}

	ch->RemoveAffect(AFFECT_RUNE);

	for(size_t i = eBuffs::BUFF_START; i < eBuffs::BUFF_END; i++)
	{
		ch->RemoveRuneBonus(i);
	}

	ch->ComputePoints();
	std::vector<int> Active_runes;
	
	size_t pos = 0;
	size_t w = 0;

	while ((pos = set.find('_')) != std::string::npos)
	{
		Active_runes.push_back(stoi(set.substr(0, pos)));
		w++;
		set.erase(0, pos + 1);
	}

	int p_point = 0, s_point = 0;

	if(page == 0)
	{
		p_point = POINT_RUNE_PAGE1_ROW1;
		if(keystone != 0)
		{
			if(ch->GetPoint(POINT_RUNE_PAGE1_KEYSTONE1 + keystone - 1) == 1)
			{
				GiveBonus(ch, page, keystone);
			}
		}
	}
	else if(page == 1)
	{
		p_point = POINT_RUNE_PAGE2_ROW1;
		if(keystone != 0)
		{
			if(ch->GetPoint(POINT_RUNE_PAGE2_KEYSTONE1 + keystone - 1) == 1)
			{
				GiveBonus(ch, page, keystone);
			}
		}
	}
	else
	{
		p_point = POINT_RUNE_PAGE3_ROW1;
		if(keystone != 0)
		{
			if(ch->GetPoint(POINT_RUNE_PAGE3_KEYSTONE1 + keystone - 1) == 1)
			{
				GiveBonus(ch, page, keystone);
			}
		}
	}
	
	if(sec_page == 0)
	{
		s_point = POINT_RUNE_PAGE1_ROW1;
	}
	else if(sec_page == 1)
	{
		s_point = POINT_RUNE_PAGE2_ROW1;
	}
	else
	{
		s_point = POINT_RUNE_PAGE3_ROW1;
	}
	
	for(size_t i = 0; i < Active_runes.size(); i++)
	{
		if(i < 3)
		{
			int rune = Active_runes[i];
			if(rune == 0)
			{
				continue;
			}
			
			if(ch->GetPoint(p_point + i) == 1)
			{
				GiveBonus(ch, page, rune + 3);
			}
		}
		else
		{
			int rune = Active_runes[i];

			if(rune == 0)
			{
				continue;
			}
			
			if(ch->GetPoint(s_point + i - 3) == 1)
			{
				GiveBonus(ch, sec_page, rune + 3);
			}
		}
	}
}

void CRuneSystem::GiveBonus(LPCHARACTER ch, int page, int rune)
{
	if(page > 2 || page < 0)
	{
		return;
	}
	
	if(rune > 12 || rune < 1)
	{
		return;
	}

	Rune_struct rn = GetRuneInfo(page, rune);

	for(auto bonus : rn.bonuses)
	{
		int type = bonus.first;
		int value = bonus.second;

		if(type > 0)
		{
			ch->AddAffect(AFFECT_RUNE, aApplyInfo[type].bPointType, value, 0, 3600 * 60 * 60, 0, true, true);
		}
		else
		{
			ch->AddRuneBonus(-type, value);
			if(-type == BUFF_COOLDOWN_RESET)
			{
				int chance = number(1, 100);

				if(chance >= 100 - value)
				{
					ch->PointChange(POINT_CASTING_SPEED, 10000);
				}
			}
			ch->ComputePoints();
		}
	}
}
#endif
