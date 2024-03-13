-- Task: List records with a name value
-- Lists all records of the table second_table from the database hbtn_0c_0 where rows without a name value are excluded. Results display the score and the name (in this order) with records listed by descending score.

SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
