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