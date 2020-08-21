-- The IN operator allows you to specify multiple values in a WHERE clause.
SELECT column_name(s)
FROM table_name
WHERE column_name IN (value1, value2, ...);

-- OR

SELECT column_name(s)
FROM table_name
WHERE column_name IN (SELECT STATEMENT); 