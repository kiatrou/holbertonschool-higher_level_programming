-- This is a script thatlists all Comedy shows in the database hbtn_0d_tvshows.
SELECT 
    s.title
FROM 
    tv_shows s
    INNER JOIN tv_show_genres tsg ON s.id = tsg.show_id
    INNER JOIN tv_genres g ON tsg.genre_id = g.id
WHERE 
    g.name = 'Comedy'
ORDER BY 
    s.title ASC;