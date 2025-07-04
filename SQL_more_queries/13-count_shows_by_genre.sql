-- This is a script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
SELECT 
    g.name AS genre,
    COUNT(tsg.show_id) AS number_of_shows
FROM 
    tv_genres g
    INNER JOIN tv_show_genres tsg ON g.id = tsg.genre_id
GROUP BY 
    g.id, g.name
ORDER BY 
    number_of_shows DESC;