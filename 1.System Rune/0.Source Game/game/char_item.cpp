// Find //
		const auto apply_value = item->GetValue(2);

// Replace //
#ifdef ENABLE_RUNE_SYSTEM_REMOVED /*** If leave this function enabled get double potion bonus if rune is enabled or diasabled ***/
		const auto apply_value = item->GetValue(2) + (item->GetValue(2) * (100 + GetPoint(POINT_POTION_BONUS)) / 100);
#else
		const auto apply_value = item->GetValue(2);
#endif

// Find //
		const auto apply_value = item->GetValue(2);

// Replace //
#ifdef ENABLE_RUNE_SYSTEM_REMOVED /*** If leave this function enabled get double potion bonus if rune is enabled or diasabled ***/
			const auto apply_value = item->GetValue(2) + (item->GetValue(2) * (100 + GetPoint(POINT_POTION_BONUS)) / 100);
#else
			const auto apply_value = item->GetValue(2);
#endif

// Find //
			const auto affectValue = item->GetValue(2);

// Replace //
#ifdef ENABLE_RUNE_SYSTEM_REMOVED /*** If leave this function enabled get double potion bonus if rune is enabled or diasabled ***/
			const auto affectValue = item->GetValue(2) + (item->GetValue(2) * (100 + GetPoint(POINT_POTION_BONUS)) / 100);
#else
			const auto affectValue = item->GetValue(2);
#endif