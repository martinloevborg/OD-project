CREATE DATABASE IF NOT EXISTS pDatabase;
USE pDatabase;
CREATE TABLE persontb(
    PersonID SERIAL PRIMARY KEY,
    Firstname CHAR(100),
    Lastname CHAR(100)
);