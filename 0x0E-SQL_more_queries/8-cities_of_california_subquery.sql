-- Lists all cities of California found in the database
-- Uses subquery to find state_id for California
SELECT id, name
FROM cities
WHERE state_id = (
    SELECT id
    FROM states
    WHERE name = 'California'
)
ORDER BY id ASC;
