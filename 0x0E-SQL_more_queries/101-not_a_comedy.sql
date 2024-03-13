-- Lists all shows without the genre Comedy in the database hbtn_0d_tvshows.

-- Get shows linked to Comedy
SELECT tv_show_id
FROM tv_show_genres
WHERE genre_id = (SELECT id FROM tv_genres WHERE name = 'Comedy');

-- Get shows without Comedy genre
SELECT DISTINCT tv_shows.title
FROM tv_shows
WHERE id NOT IN (
    SELECT tv_show_id
    FROM tv_show_genres
    WHERE genre_id = (SELECT id FROM tv_genres WHERE name = 'Comedy')
)
ORDER BY tv_shows.title ASC;
