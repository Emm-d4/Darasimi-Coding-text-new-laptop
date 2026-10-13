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

Destination = pd.read_sql("SELECT * FROM Destination", conn)
Attraction = pd.read_sql("SELECT * FROM attraction", conn)

print("Destination table:")
print(Destination)
print()

print("Attraction Table:")
print(Attraction)
print()

# ---- PART 2: INNER JOIN ----

inner = pd.read_sql(
    "SELECT Destination.Destination_name, Attraction.attraction_title " 
    "FROM Destination INNER JOIN Attraction ON Destination.Destination_id = Destination.Destination_id",
    conn
)
print("INNER JOIN - Destination matched with their attraction:")
print(inner)
print()