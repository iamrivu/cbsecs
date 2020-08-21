-- The PRIMARY KEY constraint uniquely identifies each record in a table.
-- Primary keys must contain UNIQUE values, and cannot contain NULL values.
-- A table can have only ONE primary key; and in the table, this primary key can consist of single or multiple columns (fields).

-- EX IN MYSQL
CREATE TABLE Persons (
    ID int NOT NULL,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int,
    PRIMARY KEY (ID)
); 