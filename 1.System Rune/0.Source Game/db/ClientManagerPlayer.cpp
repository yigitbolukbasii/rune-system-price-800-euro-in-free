/* Find In : size_t CreatePlayerSaveQuery(char* pszQuery, size_t querySize, TPlayerTable* pkTab)
// Find */
				   "horse_skill_point = %d, "
// Add After //
#ifdef ENABLE_RUNE_SYSTEM
					"r_available = '%s', "
#endif
// To be like this //
				   "horse_hp_droptime = %u, "
				   "horse_stamina = %d, "
				   "horse_skill_point = %d, "
#ifdef ENABLE_RUNE_SYSTEM
					"r_available = '%s', "
#endif
// Find //
				   pkTab->horse_skill_point

// Add After //
#ifdef ENABLE_RUNE_SYSTEM
					,pkTab->cAvailableRunes
#endif
// ----------------------------------------------------------------------------------------------------------------------- //

/* Find In : void CClientManager::QUERY_PLAYER_LOAD(CPeer* peer, DWORD dwHandle, TPlayerLoadPacket* packet)

Find */
			"horse_skill_point, "

// Add After //
#ifdef ENABLE_RUNE_SYSTEM
			"r_available, "
#endif

// ----------------------------------------------------------------------------------------------------------------------- //

/* Find In : bool CreatePlayerTableFromRes(MYSQL_RES* res, TPlayerTable* pkTab)

Find */
	str_to_number(pkTab->horse_skill_point, row[col++]);

// Add After //
#ifdef ENABLE_RUNE_SYSTEM
	strlcpy(pkTab->cAvailableRunes, row[col++], sizeof(pkTab->cAvailableRunes));
#endif