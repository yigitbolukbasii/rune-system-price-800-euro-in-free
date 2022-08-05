#pragma once

#ifdef ENABLE_RUNE_SYSTEM
class CRuneSystem : public singleton<CRuneSystem>
{
	public:
		enum eBuffs
		{
			BUFF_START = 0,
			BUFF_RESTORE_HEALTH = 1,
			BUFF_COOLDOWN_RESET = 2,
			BUFF_BLOCK_DESTROY = 3,
			BUFF_ATTACK = 4,
			BUFF_TRUE_DAMAGE = 5,
			BUFF_SPEED = 6,
			BUFF_HALF_DAY = 7,
			BUFF_STRONGER = 8,
			BUFF_DROP_BOSS = 9,
			BUFF_CRIT_DAMAGE = 10,
			BUFF_STANDARD_EQUIPMENT = 11,
			BUFF_MOUNT_BONUS = 12,
			BUFF_PET_BONUS = 13,
			BUFF_LEADER_BONUS = 14, 
			BUFF_COSTUME_BONUS = 15,
			BUFF_MORE_POTIONS = 16,
			BUFF_END
		};

		enum eDamageFlag
		{
			DAMAGE_NORMAL	= (1 << 0),
			DAMAGE_POISON	= (1 << 1),
			DAMAGE_DODGE	= (1 << 2),
			DAMAGE_BLOCK	= (1 << 3),
			DAMAGE_PENETRATE= (1 << 4),
			DAMAGE_CRITICAL = (1 << 5),
		};

	private:
		typedef struct Rune_struct
		{
			unsigned int runeID;
			unsigned int costValue;
			std::map<DWORD, int> items;
			std::map<DWORD, int> bonuses;
		}Rune_struct;

		std::vector<std::vector<Rune_struct>> Runes{ {}, {}, {} };
		Rune_struct GetRuneInfo(int page, int runeID);

	public:
		CRuneSystem();
		~CRuneSystem();
		
	public:
		void LoadRunes();
		bool GrantRune(LPCHARACTER ch, int page, int row);
		bool GrantKeystone(LPCHARACTER ch, int page, int keystone);
		void ActivateBonus(LPCHARACTER ch, int page, int sec_page, int keystone, std::string set);
		void GiveBonus(LPCHARACTER ch, int page, int rune);
};
#endif
