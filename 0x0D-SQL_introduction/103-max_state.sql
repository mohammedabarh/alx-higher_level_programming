-- Script to display maximum temperature of each state
-- Orders by state name
SELECT state, MAX(value) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state;
