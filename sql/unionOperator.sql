-- The UNION operator is used to combine the result-set of two or more SELECT statements.

--     Each SELECT statement within UNION must have the same number of columns
--     The columns must also have similar data types
--     The columns in each SELECT statement must also be in the same order

SELECT column_name(s) FROM table1
UNION
SELECT column_name(s) FROM table2; 

-- The UNION operator selects only distinct values by default. To allow duplicate values, use UNION ALL
SELECT column_name(s) FROM table1
UNION ALL
SELECT column_name(s) FROM table2; 

-- EX
SELECT City FROM Customers
UNION ALL
SELECT City FROM Suppliers
ORDER BY City;