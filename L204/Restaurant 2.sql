CREATE TABLE IF NOT EXISTS restaurant (
    RESTAURANT_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    RESTAURANT_NAME TEXT,
    NEIGHBOURHOOD TEXT,
    CUISINE TEXT,
    REVEIW REAL,
    PRICE TEXT,
    HEALTH TEXT
);


INSERT INTO restaurant (RESTAURANT_NAME, NEIGBOURHOOD, CUISINE, REVIEW, PRICE, HEALTH) VALUES
    ("Layar", "Jakarta", "Seafood", 4.4, "$$$$", "A"),
    ("RM Surya", "Jakarta", "Indonesian", 4.5, "$$$", "A"),
    ("Ahjumma Kitchen", "Surabaya", "Korean", 3.5, "$$", "A"),
    ("Pizza e Birra", "Surabaya", "Pizza", 4, "$$$", "B"),
    ("Spice Affair", "Bandung", "Indian", 3.9, "$", "A"),
    ("Prabhu Curry House", "Bangung", "Indian", 4.6, "$$$", "B"),
    ("Moi Garden Hakka", "Surabaya", "Chinese", 3.0, "$$", "B"),
    ("L'Osteria Pizza e Cucina", "Ubud", "Italian", 4.9, "$$$$", "B"),
    ("Paparons Pizza", "Surabaya", "Pizza", 3.8, "$$$", "A"),
    ("Warung Italia", "Ubud", "Italian", 3.8, "$$$", "A");

-- Select all records from the restaurant table
SELECT * FROM restaurant;

-- distinct neighborhoods from the restaurant table
SELECT DISTINCT NEIGHBOURHOOD FROM restaurant;

-- Select distinct cusunes from the restaurant table
SELECT DISTINCT CUISINE FROM restaurant;

-- Select all records with Chinese cuisine
SELECT * FROM restaurant WHERE CUISINE = "Chinese";

--Select all records with a review ratingnof 4 or higher
SELECT * FROM restaurant WHERE REVIEW >= 4;

-- Select all records with Itakain cuisine and $$$ price
SELECT * FROM restaurant WHERE CUISINE = "Italian" AND PRICE = "$$$";