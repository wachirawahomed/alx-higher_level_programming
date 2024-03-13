-- Task: Temperatures #1
-- Displays the top 3 cities with the highest average temperatures during July and August ordered by temperature (descending).

SELECT city, ROUND(AVG(temperature), 4) AS avg_temp
FROM temperatures
WHERE MONTH(date) IN (7, 8)
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
