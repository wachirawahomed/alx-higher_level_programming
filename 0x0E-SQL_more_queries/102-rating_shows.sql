-- Lists all shows from hbtn_0d_tvshows_rate by their rating.

SELECT tv_shows.title, SUM(tvshow_ratings.rating) AS rating_sum
FROM tv_shows
JOIN tvshow_ratings ON tv_shows.id = tvshow_ratings.show_id
GROUP BY tv_shows.title
ORDER BY rating_sum DESC;
