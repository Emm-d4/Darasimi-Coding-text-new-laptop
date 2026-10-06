import sqlite3
import pandas as pd

# --- PART 1: What is a JOIN - Build and Explore the Tables

conn = sqlite3.connect(':memory:')

conn.execute("""
            CREATE TABLE author (
                    author_id   INTEGER PRIMARY KEY,
                    author_name TEXT NOT NULL UNIQUE
                    )
                    """)

conn.execute("""
            CREATE TABLE book (
                book_id   INTEGER PRIMARY KEY,
                book_title  TEXT NOT NULL,
                author_id   INTEGER
                )
                """)

conn.executemany("INSERT INTO author VALUES (?, ?)", [
    (1, 'Ronald Dahl'),
    (2, 'J.K. Rowling'),
    (3, 'Rick Riordan'),
    (4, 'Jeff Kinney'),
    (5, 'Dav Pilkey'),
    (6, 'Lemony Snicket'),
])

conn.executemany("INSERT INTO book VALUES (?, ?, ?)", [
    (1, 'Charlie and the Chocolate Factory',        1),
    (2, 'James and the Giant Peach',                1),
    (3, 'Harry potter and the Philosophers Stone',  2),
    (4, 'Harry potter and the Chamber of Secrets',  2),
    (5, 'The Lightning Thief',                      3),
    (6, 'The Sea of Monsters',                      3),
    (7, 'Diary of a wimpy kid',                     4),
])

conn.commit()

authors = pd.read_sql("SELECT * FROM author", conn)
books = pd.read_sql("SELECT * FROM book", conn)

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