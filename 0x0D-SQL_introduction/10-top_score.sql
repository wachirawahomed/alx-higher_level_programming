-- Task: List records by top score
-- Lists all records of the table second_table from the database
-- hbtn_0c_0, ordered by score (top first).

SELECT score, name FROM hbtn_0c_0.second_table ORDER BY score DESC;
