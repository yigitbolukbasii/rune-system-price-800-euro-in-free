// Add //
#ifdef ENABLE_RUNE_SYSTEM
#include "new_rune_system.h"
#endif

// Find //
ACMD(do_ride)
{
}

// Add After //
#ifdef ENABLE_RUNE_SYSTEM
ACMD(do_activate_rune)
{
	if(!ch)
	{
		return;
	}

	char arg1[256];
	one_argument(argument, arg1, sizeof(arg1));

	if (!*arg1)
	{
		return;
	}

	std::string runes = arg1;
	std::vector<int> Selected;

	size_t pos = 0;
	size_t w = 0;

	while ((pos = runes.find('_')) != std::string::npos)
	{
		Selected.push_back(stoi(runes.substr(0, pos)));
		w++;
		runes.erase(0, pos + 1);
	}

	char returning[256];

	if(Selected.size() >= 8)
	{
		snprintf(returning, sizeof(returning), "%d_%d_%d_%d_%d_", Selected[3], Selected[4], Selected[5], Selected[6], Selected[7]);
		CRuneSystem::instance().ActivateBonus(ch, Selected[0], Selected[1], Selected[2], returning);
	}
	else
	{
		ch->ChatPacket(CHAT_TYPE_INFO, "RUNE ERROR %s -> %d", arg1, Selected.size());
	}
}
#endif


