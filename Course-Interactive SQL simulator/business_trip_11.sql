SELECT name, SUM(per_diem * (DATEDIFF(date_last, date_first) + 1)) AS Сумма
FROM trip
GROUP BY name
HAVING name IN (
    SELECT name
    FROM trip
    GROUP BY NAME
    HAVING COUNT(name) > 3
)
ORDER BY Сумма DESC
