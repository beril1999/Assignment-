UPDATE vaccinations
SET daily_vaccinations = (
  SELECT MIN(daily_vaccinations)
  FROM vaccinations AS v2
  WHERE v2.country = vaccinations.country
  AND daily_vaccinations IS NOT NULL
)
WHERE daily_vaccinations IS NULL;