SELECT column1, column2, ...
FROM table_name
ORDER BY column1, column2, ... ASC|DESC; 

-- EX
SELECT * FROM Customers
ORDER BY Country DESC; 

SELECT * FROM Customers
ORDER BY Country ASC, CustomerName DESC; 