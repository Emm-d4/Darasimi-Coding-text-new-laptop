CREATE TABLE IF NOT EXISTS STUDENTS  (
    ROLL_NO TEXT PRIMARY KEY,
    SNAME TEXT NOT NULL,
    SADDRESS TEXT,
    PHONE TEXT,
    AGE INTEGER
);

-- Insert sample data into the STUDENT table
INSERT INTO STUDENTS(ROLL_NO, SNAME, SADDRESS, PHONE, AGE) VALUES
    ("1", "Andrew", "Jakarta", "+62-123456666", 17),
    ("2", "Jack", "Surabaya", "+62-193856690", 18),
    ("3", "Ashly", "Semarang", "+62-103456787", 20),
    ("4", "Randy", "pelembang", "+62-18345687", 18),
    ("5", "Jessica", "Kuta", "+62-156789666", 20),
    ("6", "Abdul", "Surabaya", "+62-12343945", 18);

--Select all records from the STUDENTS table to verify insertion
SELECT * FROM STUDENTS;

--Query students who are 18 years old and live in Surabaya
SELECT * FROM STUDENTS WHERE AGE = 18 AND SADDRESS = "Surabaya";

-- Query students who are 18 years old and named Jack
SELECT * FROM STUDENTS WHERE AGE= 18 AND SNAME = "Jack";

-- Query students who are named Jack or Randy
SELECT * FROM STUDENTS WHERE SNAME = "Jack" OR SNAME = "Randy";