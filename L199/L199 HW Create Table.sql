CREATE TABLE IF NOT EXISTS Student (
    RegNum TEXT PRIMARY KEY,
    SName TEXT,
    Grade INTEGER,
    Mark TEXT
);

insert into Student(RegNum, SName, Grade, Mark) values
("S-9001", "Oliver Smith", 9, "A+"),
("S-9002", "Amelia Johnson, 10, "B+"),
("S-9003", "Harry Williams", 11, "A+"),
("S-9004", "Emily Brown", 11, "A+"),
("S-9005", "George Taylor", 11, "A+"),
("S-9006", "Isla Wilson", 11, "A+"),
("S-9007", "Jack Davies", 11, "A+"),
("S-9008", "Sophia Evans", 11, "A+"),
("S-9009", "Henry Robinson", 11, "A+"),
("S-9010", "Lily Thompson", 11, "A+");

-- displaying data where mark is A+
select * from Student where Mark="A+";