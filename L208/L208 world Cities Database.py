# --- PART 1: Create the Table with constraints ---
# SQL constraints are rules written instde CREATE TABLE#

import sqlite3
import pandas as pd

conn = sqlite3.connect(r"C:\Users\famil\Desktop\Darasimi-Coding-text-new-laptop\L208\cities.db")

conn.execute("DROP TABLE IF EXISTS City;")

conn.execute("""
CREATE TABLE City (
    City_Id     INTEGER     PRIMARY KEY,
    City_Name   TEXT       NOT NULL UNIQUE,
    Country     TEXT        NOT NULL,
    Population  INTEGER,
    Is_Capital  TEXT        DEFULT 'No' 
);
""")
conn.commit()
print("Table created succefully")

# --- PART 2: INSERT -- Adding Rows To the Table ---
conn.execute("INSERT INTO City VALUES (1, 'Tokyo',      'Japan',   13960000,    'Yes');")

conn.execute("INSERT INTO City VALUES (2, ' Nairobi',      'Kenya',   4397000,    'Yes');")

conn.execute("INSERT INTO City VALUES (3, 'Mumbai',      'India',   20667656,    'No');")

conn.execute("INSERT INTO City VALUES (4, 'Sao paulo',      'Brazil',   12325232,    'No');")

conn.execute("INSERT INTO City VALUES (5, 'London',      'UK',   9541000,    'Yes');")

conn.execute("INSERT INTO City (City_Id, City_Name, Country) VALUES (6,'Sydney',      'Australia');")

conn.commit()
print("Rows inserted successfully!")

cities = pd.read_sql("SELECT * FROM City;", conn)
print(cities)

#---PART 3: PRIMARY KEY in Action ---0
# PRIMARY KEY uniquely identifies every row.
# No two rows can share the same city_Id.#
# The column alsocnnot ne NULL.
#Trying to insert a duplicate PRIMARY KEY raises an error

print("\n-- Testing PRIMARY KEY --")
try:
    conn.excute("INSERT INTO City VALUES (1, 'cairo', 'Egypt', 2132000, 'Yes');")
    conn.commit()
except Exception as e:
    conn.rollback()
    print("Rejected:", e)
    print("City_Id 1 already belongs to Tokyo -- PRIMARY KEY must be unique.")

# --- PART 4: NOT NULL and UNIQUE in Action ---

print("\n--- Testing NOT NULL ---")
try:
    conn.execute("INSERT INTO City VALUES (7, 'Berlin', NULL, 3645000, 'Yes');")
    conn.commit()
except Exception as e:
    conn.rollback()
    print("Rejected:", e) 
    print("Country is NOT NULL -- every row must provide a country value.")

print("\n--Testing UNIQUE")
try:
    conn.execute("INSERT INTO City VALUES (8, 'Tokyo', 'Japan', 99999, 'No');")
    conn.commit()
except Exception as e:
    conn.rollback()
    print("Rejected:", e)
    print("City_Name is UNIQUE -- 'Tokyo' is already in the table.")

conn.close()