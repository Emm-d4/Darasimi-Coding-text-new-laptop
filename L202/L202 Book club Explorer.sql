-- ----PART 1: Build and Explore the Table ----

CREATE TABLE IF NOT EXISTS book (
    book_id INTEGER PRIMARY KEY,
    title   TEXT    NOT NULL,
    genre   TEXT    NOT NULL,
    rating   REAL    NOT NULL,
    pages   INTEGER    NOT NULL,
    pub_year   INTEGER    NOT NULL
);

INSERT INTO book VALUES (1, 'Dragon Quest',  'Fantasy',  9.2, 312, 2021);
INSERT INTO book VALUES (2, 'Code Wizards',  'Sci-Fi',  8.5, 280, 2020);
INSERT INTO book VALUES (3, 'Ocean Deep',  'Adventure',  7.8, 195, 2022);
INSERT INTO book VALUES (4, 'Star Rangers',  'Sci-Fi',  9.5, 340, 2019);

SELECT * FROM book;

-- ----PART 2: ORDER BY ----

-- Sort all the books lowest rating first (ASC is the default)
SELECT title, rating FROM book ORDER BY rating ASC;

-- Sort all books highest rating first
SELECT title, rating FROM book ORDER BY rating DESC;

-- sort by genre A-Z then highest rating first within each genre
SELECT title, genre, rating FROM book ORDER BY genre ASC, rating DESC;

-- ----PART 3: LIMIT ----
 
-- Top 3 highest-rated books
SELECT title, rating FROM book ORDER BY rating DESC LIMIT 3;

-- 3 oldest by publication year
SELECT title, pub_year FROM book ORDER BY pub_year ASC LIMIT 5;

