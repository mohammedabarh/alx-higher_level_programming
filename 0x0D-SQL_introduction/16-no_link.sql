-- Script to list all records of second_table
-- Excludes rows without name value
-- Displays score and name, ordered by descending score
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
