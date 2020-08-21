-- A FOREIGN KEY is a key used to link two tables together.
-- A FOREIGN KEY is a field (or collection of fields) in one table that refers to the PRIMARY KEY in another table.
-- The table containing the foreign key is called the child table, and the table containing the candidate key is called the referenced or parent table.

-- EX IN MYSQL
CREATE TABLE Orders (
    OrderID int NOT NULL,
    OrderNumber int NOT NULL,
    PersonID int,
    PRIMARY KEY (OrderID),
    FOREIGN KEY (PersonID) REFERENCES Persons(PersonID)
); 

-- DEMO TABLES

-- "Persons" table:
-- PersonID 	LastName 	FirstName 	Age
-- 1 	        Hansen 	        Ola 	30
-- 2 	        Svendson 	    Tove 	23
-- 3 	        Pettersen 	    Kari 	20

-- "Orders" table:
-- OrderID 	    OrderNumber 	PersonID
-- 1 	            77895 	        3
-- 2 	            44678 	        3
-- 3 	            22456 	        2
-- 4 	            24562 	        1