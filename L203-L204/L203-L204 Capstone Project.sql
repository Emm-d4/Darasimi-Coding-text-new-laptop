CREATE TABLE IF NOT EXISTS Salesperson (
    Salesperson_id TEXT PRIMARY KEY,
    name TEXT,
    city TEXT,
    Comission REAL
);  

INSERT INTO Salesperson (Salesperson_id, name, city, Comission) VALUES
    ("7001", "Jessica Wong", "Berlin", 0.18),
    ("7002", "James White", "Paris", 0.17),
    ("7003", "Andrew Smith", "London", 0.17),
    ("7004", "Alex McGrager", "New york", 0.18),
    ("7005", "Paul Adam", "Copenhagen", 0.17),
    ("7006", "Tristan Alexander", "Moscow", 0.11);

CREATE TABLE IF NOT EXISTS Cust (
    customer_id TEXT,
    cust_name TEXT PRIMARY KEY
    city TEXT,
    grade INTEGER,
    Salesperson_id TEXT,
    FOREIGN KEY (Salesperson_id) REFERENCES Salesperson_id)
    );

INSERT INTO (customer_id, cust_name, city, grade, Salesperson_id) VALUES
    ("C1001", "Jay Idzes", "New York", 100, "7004"),
    ("C1002", "Justin Hubner", "London", 300, "7003"),
    ("C1003", "Sandy walsh", "Moscow", 200, "7006"),
    ("C1004", "Garaga", "Paris", NULL, "7002"),
    ("C1005", "Zoe Saldana", "Califonia", 100, "7004"),
    ("C1006", "Towel Toyyib", "London", 100, "7004"),
    ("C1007", "Brad Pitt", "New York", 100, "7004"),
    ("C1008", "Andrew Smith", "New York", 100, "7004"),
    ("C1009", "Ragnar", "New York", 100, "7004");
