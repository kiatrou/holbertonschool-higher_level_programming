-- This is a script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
SELECT genre_id AS genre, COUNT(show_id) AS number_of_shows
FROM tv_show_genres
GROUP BY genre_id
ORDER BY number_of_shows DESC;