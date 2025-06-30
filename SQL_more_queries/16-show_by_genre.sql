-- This is a scrip that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows
SELECT 
    s.title,
    g.name
FROM 
    tv_shows s
    LEFT JOIN tv_show_genres tsg ON s.id = tsg.show_id
    LEFT JOIN tv_genres g ON tsg.genre_id = g.id
ORDER BY 
    s.title ASC, g.name ASC;