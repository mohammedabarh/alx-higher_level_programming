-- Script to display average temperature by city
-- Orders results by temperature descending
SELECT city, AVG(value) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
