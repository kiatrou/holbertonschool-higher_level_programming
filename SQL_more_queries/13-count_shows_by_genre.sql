-- This is a script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
SELECT genre.name AS genre,
COUNT(tv_show_genres.show_id) AS number_of_shows
FROM genre
JOIN tv_show_genres ON genre.id = tv_show_genres.genre_id
GROUP BY genre.name
ORDER BY number_of_shows DESC;