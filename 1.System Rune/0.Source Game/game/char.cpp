// Find //
	memset(&m_tvLastSyncTime, 0, sizeof(m_tvLastSyncTime));
	
// Add After //
#ifdef ENABLE_RUNE_SYSTEM
	m_dwRuneBonuses.clear();
	m_iStrike.clear();
	m_dwRuneString = "";
#endif

// Find //
	tab.horse = GetHorseData();

// Add After //
#ifdef ENABLE_RUNE_SYSTEM
	strlcpy(tab.cAvailableRunes, GetRunes().c_str(), sizeof(tab.cAvailableRunes));
#endif

// Find //

	for (int i = POINT_ST; i < POINT_MAX_NUM; ++i)
	{
		pack.points[i] = GetPoint(i);
	}

// Add After //

#ifdef ENABLE_RUNE_SYSTEM
	for (int w = 0; w <= 17; ++w)
	{
		BYTE bType = POINT_RUNE_PAGE1_KEYSTONE1 + w;
		pack.points[bType] = GetPoint(bType);
	}
#endif

// Find //
	SetXYZ(t->x, t->y, t->z);

// Add After //
#ifdef ENABLE_RUNE_SYSTEM
	m_dwRuneString = t->cAvailableRunes;
	size_t pos = 0;
	size_t w = 0;
	std::string s = m_dwRuneString;
	while ((pos = s.find(',')) != std::string::npos)
	{
		SetPoint(POINT_RUNE_PAGE1_KEYSTONE1 + w, stoi(s.substr(0, pos)));
		w++;
		s.erase(0, pos + 1);
	}
#endif

// Find //
	long lSPRecovery = GetPoint(POINT_SP_RECOVERY);

// Add After //
#ifdef ENABLE_RUNE_SYSTEM
	std::vector<int> vRunes;
#ifdef ENABLE_FAKE_PC
	if (IsPC() || FakePC_Check())
#else
	if (IsPC())
#endif
	{
		for (int w = 0; w <= 17; ++w)
		{
			BYTE bType = POINT_RUNE_PAGE1_KEYSTONE1 + w;
			vRunes.push_back(GetPoint(bType));
		}
		vRunes.push_back(0);
	}
#endif

// Find //
	SetPoint(POINT_SP_RECOVERY, lSPRecovery);

// Add After //

#ifdef ENABLE_RUNE_SYSTEM
#ifdef ENABLE_FAKE_PC
	if (IsPC() || FakePC_Check())
#else
	if (IsPC())
#endif
	{
		for (int w = 0; w <= 17; ++w)
		{
			BYTE bType = POINT_RUNE_PAGE1_KEYSTONE1 + w;
			SetPoint(bType, vRunes[w]);
		}
		vRunes.clear();
	}
#endif

// Find //

	case POINT_COSTUME_ATTR_BONUS:
	{
		int old_val = GetPoint(type);
		SetPoint(type, old_val + amount);
		val = GetPoint(type);
		BuffOnAttr_ValueChange(type, old_val, val);
	}
	break;

// Add After //

#ifdef ENABLE_RUNE_SYSTEM
	case POINT_RUNE_PAGE1_KEYSTONE1:
	case POINT_RUNE_PAGE1_KEYSTONE2:
	case POINT_RUNE_PAGE1_KEYSTONE3:
	case POINT_RUNE_PAGE2_KEYSTONE1:
	case POINT_RUNE_PAGE2_KEYSTONE2:
	case POINT_RUNE_PAGE2_KEYSTONE3:
	case POINT_RUNE_PAGE3_KEYSTONE1:
	case POINT_RUNE_PAGE3_KEYSTONE2:
	case POINT_RUNE_PAGE3_KEYSTONE3:
	case POINT_RUNE_PAGE1_ROW1:
	case POINT_RUNE_PAGE1_ROW2:
	case POINT_RUNE_PAGE1_ROW3:
	case POINT_RUNE_PAGE2_ROW1:
	case POINT_RUNE_PAGE2_ROW2:
	case POINT_RUNE_PAGE2_ROW3:
	case POINT_RUNE_PAGE3_ROW1:
	case POINT_RUNE_PAGE3_ROW2:
	case POINT_RUNE_PAGE3_ROW3:
	{
		SetPoint(type, amount);
		val = GetPoint(type);
	}
	break;
#endif

// Add Anywhere //
#ifdef ENABLE_RUNE_SYSTEM
bool CHARACTER::GetStrikeByVid(DWORD dwTargetVID, DWORD * iAmount)
{
	auto it = m_iStrike.find(dwTargetVID);

	if (it == m_iStrike.end())
	{
		return false;
	}

	*iAmount = it->second;
	return true;
}

void CHARACTER::RegisterStrike(DWORD dwTargetVID)
{
	DWORD iCount = 0;
	DWORD iTotalAmount = 0;

	if (!GetStrikeByVid(dwTargetVID, &iCount))
	{
		m_iStrike.insert(std::make_pair(dwTargetVID, 1));
	}

	iTotalAmount = iCount += 1;
	m_iStrike[dwTargetVID] = iTotalAmount;
}

void CHARACTER::ResetStrikes(DWORD dwTargetVID)
{
	auto it = m_iStrike.find(dwTargetVID);
	if (it != m_iStrike.end())
	{
		m_iStrike.erase(it);
	}
}

std::string CHARACTER::GetRunes()
{
	std::string return_value = "";
	for(int i = POINT_RUNE_PAGE1_KEYSTONE1; i <= POINT_RUNE_PAGE3_ROW3; i++)
	{
		return_value += std::to_string(GetPoint(i)) + ",";
	}
	return return_value;
}

void CHARACTER::EnableRuneRow(int bRow)
{
	SetPoint(POINT_RUNE_PAGE1_KEYSTONE1 + bRow, 1);
}

void CHARACTER::AddRuneBonus(int bType, int bValue)
{
	auto it = m_dwRuneBonuses.find(bType);
	if (it == m_dwRuneBonuses.end())
	{
		m_dwRuneBonuses.insert(std::make_pair(bType, bValue));
	}
}

void CHARACTER::RemoveRuneBonus(int bType)
{
	auto it = m_dwRuneBonuses.find(bType);
	if (it != m_dwRuneBonuses.end())
	{
		m_dwRuneBonuses.erase(it);
	}
}

int CHARACTER::GetBonusValue(int bType)
{
	auto it = m_dwRuneBonuses.find(bType);
	if (it != m_dwRuneBonuses.end())
	{
		return it->second;
	}
	return 0;
}

bool CHARACTER::HasRuneBonus(int bType)
{
	auto it = m_dwRuneBonuses.find(bType);
	if (it != m_dwRuneBonuses.end())
	{
		return true;
	}
	return false;
}
#endif