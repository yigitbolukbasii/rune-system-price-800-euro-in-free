// Find //
	POINT_RESIST_CLAW
	or
	POINT_BATTLE_PASS_ID
	
// Add After //
#ifdef ENABLE_RUNE_SYSTEM
	POINT_RUNE_PAGE1_KEYSTONE1,
	POINT_RUNE_PAGE1_KEYSTONE2,
	POINT_RUNE_PAGE1_KEYSTONE3,
	POINT_RUNE_PAGE2_KEYSTONE1,
	POINT_RUNE_PAGE2_KEYSTONE2,
	POINT_RUNE_PAGE2_KEYSTONE3,
	POINT_RUNE_PAGE3_KEYSTONE1,
	POINT_RUNE_PAGE3_KEYSTONE2,
	POINT_RUNE_PAGE3_KEYSTONE3,
	POINT_RUNE_PAGE1_ROW1,
	POINT_RUNE_PAGE1_ROW2,
	POINT_RUNE_PAGE1_ROW3,
	POINT_RUNE_PAGE2_ROW1,
	POINT_RUNE_PAGE2_ROW2,
	POINT_RUNE_PAGE2_ROW3,
	POINT_RUNE_PAGE3_ROW1,
	POINT_RUNE_PAGE3_ROW2,
	POINT_RUNE_PAGE3_ROW3,
#endif

// Find //
	int GetPolymorphPower() const;

// Add After //
#ifdef ENABLE_RUNE_SYSTEM
	std::string GetRunes();
	void EnableRuneRow(int bRow);
	void SetRunes(std::string bNew) { m_dwRuneString = bNew; }
	void AddRuneBonus(int bType, int bValue);
	void RemoveRuneBonus(int bType);
	bool HasRuneBonus(int bType);
	int GetBonusValue(int bType);
	void RegisterStrike(DWORD dwTargetVID);
	void ResetStrikes(DWORD dwTargetVID);
	bool GetStrikeByVid(DWORD dwTargetVID, DWORD * iAmount);
#endif

// Find //

	BYTE m_bCharType;

// Add After //

#ifdef ENABLE_RUNE_SYSTEM
	std::string m_dwRuneString;
	std::map<int, int> m_dwRuneBonuses;
	std::map<DWORD, DWORD>	m_iStrike;
#endif

// Find //
	public:
		void SendDamagePacket(LPCHARACTER pAttacker, int Damage, BYTE DamageFlag);

// Replace //
#ifdef ENABLE_RUNE_SYSTEM
public:
	void SendDamagePacket(LPCHARACTER pAttacker, int Damage, BYTE DamageFlag);
#else
private:
	void SendDamagePacket(LPCHARACTER pAttacker, int Damage, BYTE DamageFlag);
#endif
