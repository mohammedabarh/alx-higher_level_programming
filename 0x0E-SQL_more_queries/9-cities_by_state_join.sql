-- Lists all cities with their corresponding state names
-- Uses JOIN to combine data from cities and states tables
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
