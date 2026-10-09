import sqlite3
import pandas as pd

# --- PART 1: What is a JOIN - Build and Explore the Tables

conn = sqlite3.connect(':memory:')

conn.execute("""
            CREATE TABLE destination (
                    Destination_id   INTEGER PRIMARY KEY,
                    Destination_name TEXT NOT NULL UNIQUE
                    )
                    """)

conn.execute("""
            CREATE TABLE  (
                `Attraction_id`   INTEGER PRIMARY KEY,
                Attraction_title  TEXT NOT NULL,
                Destination_id   INTEGER
                )
                """)

conn.executemany("INSERT INTO Destination VALUES (?, ?)", [
    (1, 'London'),
    (2, 'Lagos'),
    (3, 'New york'),
    (4, 'Paris'),
    (5, 'washinton'),
    (1, 'newcastle'),
    (2, 'glasgow'),
    (3, 'Berlin'),
    (4, 'Tokyo'),
    (5, 'osaka')
])

conn.executemany("INSERT INTO Attraction VALUES (?, ?, ?)", [
    (1, 'London bridge',                             1),
    (2, 'Empire state',                              2),
    (3, 'Eifel tower',                               2),
    (4, 'TOKYO TOWER',                               2),
    (5, 'Berlin buildens',                           3),
])

conn.commit()

Destination = pd.read_sql("SELECT * FROM author", conn)
Attraction = pd.read_sql("SELECT * FROM book", conn)

print("Author table:")
print(authors)
print()

print("Book Table:")
print(books)
print()

# ---- PART 2: INNER JOIN ----

inner = pd.read_sql(
    "SELECT author.author_name, book.book_title " 
    "FROM author INNER JOIN book ON author.author_id = book.author_id",
    conn
)
print("INNER JOIN - author matched with their books:")
print(inner)
print()