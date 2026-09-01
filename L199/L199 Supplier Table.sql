-- creating table
CREATE TABLE supplier2 (
    SupNum TEXT PRIMARY KEY,
    SupName TEXT,
    SupStatus INTEGER,
    SupCity REAL
);

--inserting data
INSERT INTO supplier2(SupNum, SupName, SupStatus, SupCity) VALUES
("S01", "Jonathan", 20, "Cardiff"),
("S02", "Andrew", 10, "Newcastle"),
("S03", "Jessica", 15, "Manchester"),
("S04", "Jack", 30, "Liverpool"),
("S05", "Amber", 10, "Swansea"),
("S06", "Michael", 25, "Berlin"),
("S07", "Luke", 20, "Paris"),
("S08", "John", 15, "Madrid"),
("S09", "Lucy", 20, "Newcastle"),
("S010", "Nico", 10, "London");

--displaying all the data
SELECT * from supplier2;