import sqlite3
import pandas as pd

# Part 1: Create the tables

conn = sqlite3.connect(':memory:')

conn.execute("""
CREATE TABLE planet (
    planet_id INTEGER PRIMARY KEY,
    planet_name TEXT NOT NULL,
    planet_type TEXT NOT NULL,
    distance_million_km INTEGER NOT NULL
)
""")

conn.execute("""
CREATE TABLE planet_data (
    data_id INTEGER PRIMARY KEY,
    planet_id INTEGER NOT NULL,
    property_name TEXT NOT NULL,
    property_value INTEGER NOT NULL
)
""")

conn.executemany("INSERT INTO planet VALUES (?, ?, ?, ?)", [
    (1, 'Mercury', 'Terrestrial', 58),
    (2, 'Venus', 'Terrestrial', 108),
    (3, 'Earth', 'Terrestrial', 150),
    (4, 'Mars', 'Terrestrial', 228),
    (5, 'Jupiter', 'Gas Giant', 778)
])

conn.executemany("INSERT INTO planet_data VALUES (?, ?, ?, ?)", [
    (1, 1, 'Orbital Period', 88),
    (2, 1, 'Diameter', 4879),
    (3, 2, 'Orbital Period', 225),
    (4, 2, 'Diameter', 12104),
    (5, 3, 'Orbital Period', 365),
    (6, 3, 'Diameter', 12742),
    (7, 4, 'Orbital Period', 687),
    (8, 5, 'Orbital Period', 4333)
])

conn.commit()

print("Planets")
print(pd.read_sql("SELECT * FROM planet", conn))
print()

print("Planet information")
print(pd.read_sql("SELECT * FROM planet_data", conn))
print()

# Part 2: Change the column names

col_alias = pd.read_sql(
    "SELECT planet_name AS name, "
    "planet_type AS type, "
    "distance_million_km AS distance "
    "FROM planet",
    conn
)

print("Planet names and distances")
print(col_alias)

conn.close()