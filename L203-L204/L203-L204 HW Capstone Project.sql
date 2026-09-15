CREATE TABLE IF NOT EXISTS Seller_id (
    Salesperson_id TEXT PRIMARY KEY,
    name TEXT,
    city TEXT,
    Comission REAL
);  

INSERT INTO Seller_id (Seller_id, name, city, Comission) VALUES
    ("7001", "Jessica Wong", "Berlin", 0.18),
    ("7002", "James White", "Paris", 0.17),
    ("7003", "Andrew Smith", "London", 0.17),
    ("7004", "Alex McGrager", "New york", 0.18),
    ("7005", "Luka Adam", "Copenhagen", 0.17),
    ("7006", "Darasimi Roux", "Moscow", 0.11);

CREATE TABLE IF NOT EXISTS Cust (
    buyer_id TEXT,
    cust_name TEXT PRIMARY KEY
    city TEXT,
    grade INTEGER,
    Seller_id TEXT,
    FOREIGN KEY (Seller_id) REFERENCES Seller_id) 
    );

INSERT INTO (buyer_id, cust_name, city, grade, Seller_id) VALUES
    ("C1001", "Jay Idzes", "New York", 100, "7004"),
    ("C1002", "Justin Hubner", "London", 300, "7003"),
    ("C1003", "Sandy walsh", "Moscow", 200, "7006"),
    ("C1004", "Garaga", "Paris", NULL, "7002"),
    ("C1005", "Zoe Saldana", "Califonia", 100, "7004"),
    ("C1006", "Towel Toyyib", "London", 100, "7004"),
    ("C1007", "Brad Pitt", "New York", 100, "7004"),
    ("C1008", "Andrew Smith", "New York", 100, "7004"),
    ("C1009", "Ragnar", "New York", 100, "7004");
