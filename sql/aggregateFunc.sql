SELECT MIN(column_name)
FROM table_name
WHERE condition; 
-- EX
SELECT MIN(Price) AS SmallestPrice
FROM Products;

SELECT MAX(column_name)
FROM table_name
WHERE condition; 
-- EX
SELECT MAX(Price) AS LargestPrice
FROM Products; 

SELECT COUNT(column_name)
FROM table_name
WHERE condition; 
-- EX
SELECT COUNT(ProductID)
FROM Products;

SELECT AVG(column_name)
FROM table_name
WHERE condition; 
-- EX
SELECT AVG(Price)
FROM Products;

SELECT SUM(column_name)
FROM table_name
WHERE condition; 
-- EX
SELECT SUM(Quantity)
FROM OrderDetails; 