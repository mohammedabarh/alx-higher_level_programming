-- Script to display top 3 cities' temperatures during July and August
-- Orders by temperature descending
SELECT city, AVG(value) AS avg_temp
FROM temperatures
WHERE month IN (7, 8)
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
