-- Lists genres and number of shows linked to each
-- Uses COUNT and GROUP BY to get show counts per genre
SELECT tv_genres.name AS genre, COUNT(*) AS number_of_shows
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.id, tv_genres.name
ORDER BY number_of_shows DESC;
