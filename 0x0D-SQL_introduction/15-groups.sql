-- Script to list number of records with same score in second_table
-- Displays score and number of records for each score
-- Sorted by number of records (descending)
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
