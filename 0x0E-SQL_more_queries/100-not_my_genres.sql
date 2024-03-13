-- Uses the hbtn_0d_tvshows database to list all genres
-- not linked to the show Dexter

-- Get genres linked to Dexter
SELECT genre_id
FROM tv_show_genres
WHERE tv_show_id = (SELECT id FROM tv_shows WHERE title = 'Dexter');

-- Get genres not linked to Dexter
SELECT DISTINCT tv_genres.name
FROM tv_genres
WHERE id NOT IN (
    SELECT genre_id
    FROM tv_show_genres
    WHERE tv_show_id = (SELECT id FROM tv_shows WHERE title = 'Dexter')
)
ORDER BY tv_genres.name ASC;

