// Add //
#ifdef ENABLE_RUNE_SYSTEM
#include "new_rune_system.h"
#endif

// Find //
int pc_stun_player(lua_State* L)

// Add After //
#ifdef ENABLE_RUNE_SYSTEM
int pc_get_keystone(lua_State* L)
{
	LPCHARACTER ch =  CQuestManager::instance().GetCurrentCharacterPtr();
	if(!ch || !lua_isnumber(L, 1) || !lua_isnumber(L, 2))
	{
		lua_pushnumber(L, 0);
		return 1;
	}
	int page = lua_tonumber(L, 1);
	int keystone = lua_tonumber(L, 2);
	int point = POINT_RUNE_PAGE1_KEYSTONE1;
	if(page == 1)
	{
		point = POINT_RUNE_PAGE2_KEYSTONE1;
	}
	else if(page == 2)
	{
		point = POINT_RUNE_PAGE3_KEYSTONE1;
	}
	lua_pushnumber(L, ch->GetPoint(point + keystone - 1));
	return 1;
}

int pc_get_rune(lua_State* L)
{
	LPCHARACTER ch =  CQuestManager::instance().GetCurrentCharacterPtr();
	if(!ch || !lua_isnumber(L, 1) || !lua_isnumber(L, 2))
	{
		lua_pushnumber(L, 0);
		return 1;
	}
	int page = lua_tonumber(L, 1);
	int rune = lua_tonumber(L, 2);
	int point = POINT_RUNE_PAGE1_ROW1;
	if(page == 1)
	{
		point = POINT_RUNE_PAGE2_ROW1;
	}
	else if(page == 2)
	{
		point = POINT_RUNE_PAGE3_ROW1;
	}
	lua_pushnumber(L, ch->GetPoint(point + rune - 1));
	return 1;
}

int pc_set_rune(lua_State* L)
{
	LPCHARACTER ch =  CQuestManager::instance().GetCurrentCharacterPtr();
	if(!ch || !lua_isnumber(L, 1) || !lua_isnumber(L, 2))
	{
		return 0;
	}
	int page = lua_tonumber(L, 1);
	int rune = lua_tonumber(L, 2);
	CRuneSystem::instance().GrantRune(ch, page, rune);
	return 0;
}

int pc_set_keystone(lua_State* L)
{
	LPCHARACTER ch =  CQuestManager::instance().GetCurrentCharacterPtr();
	if(!ch || !lua_isnumber(L, 1) || !lua_isnumber(L, 2))
	{
		return 0;
	}
	int page = lua_tonumber(L, 1);
	int keystone = lua_tonumber(L, 2);
	CRuneSystem::instance().GrantKeystone(ch, page, keystone);
	return 0;
}

int pc_remove_rune(lua_State* L)
{
	LPCHARACTER ch =  CQuestManager::instance().GetCurrentCharacterPtr();
	if(!ch || !lua_isnumber(L, 1) || !lua_isnumber(L, 2))
	{
		return 0;
	}
	int page = lua_tonumber(L, 1);
	int rune = lua_tonumber(L, 2);
	int point = POINT_RUNE_PAGE1_ROW1;
	if(page == 1)
	{
		point = POINT_RUNE_PAGE2_ROW1;
	}
	else if(page == 2)
	{
		point = POINT_RUNE_PAGE3_ROW1;
	}
	ch->PointChange(point + rune - 1, 0);
	return 0;
}

int pc_remove_keystone(lua_State* L)
{
	LPCHARACTER ch =  CQuestManager::instance().GetCurrentCharacterPtr();
	if(!ch || !lua_isnumber(L, 1) || !lua_isnumber(L, 2))
	{
		return 0;
	}
	int page = lua_tonumber(L, 1);
	int keystone = lua_tonumber(L, 2);
	int point = POINT_RUNE_PAGE1_KEYSTONE1;
	if(page == 1)
	{
		point = POINT_RUNE_PAGE2_KEYSTONE1;
	}
	else if(page == 2)
	{
		point = POINT_RUNE_PAGE3_KEYSTONE1;
	}
	ch->PointChange(point + keystone - 1, 0);
	return 0;
}
#endif

// Find //
		{"get_killee_drop_pct", pc_get_killee_drop_pct},

// Add After //
#ifdef ENABLE_RUNE_SYSTEM
		{"get_keystone", pc_get_keystone},
		{"get_rune", pc_get_rune},
		{"set_rune", pc_set_rune},
		{"set_keystone", pc_set_keystone},
		{"remove_keystone", pc_remove_keystone},
		{"remove_rune", pc_remove_rune},
#endif