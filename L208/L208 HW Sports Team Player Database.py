# --- PART 1: Create the Table with constraints ---
# SQL constraints are rules written instde CREATE TABLE#

import sqlite3
import pandas as pd

conn = sqlite3.connect(r"C:\Users\famil\Desktop\Darasimi-Coding-text-new-laptop\L208\Team_player.db")

conn.execute("DROP TABLE IF EXISTS Player;")

conn.execute("""
CREATE TABLE City (
    Player_Id     INTEGER     PRIMARY KEY,
    Player_Name   TEXT       NOT NULL UNIQUE,
    Player_Country   TEXT        NOT NULL,
    Player_city  INTEGER,
    Player_Icon  TEXT        DEFULT 'No' 
);
""")
conn.commit()
print("Table created succefully")

# --- PART 2: INSERT -- Adding Rows To the Table ---
conn.execute("INSERT INTO Player VALUES (1, 'Victor Oshimen',      'Nigeria',   Lagos,    'No');")

conn.execute("INSERT INTO Player VALUES (2, 'Michael Olise',      'England',   London,    'No');")

conn.execute("INSERT INTO Player VALUES (3, 'Zinedine Zidane',      'France', Marseille,    'Yes');")

conn.execute("INSERT INTO Player VALUES (4, 'Yaya Toure',      'Ivory coast',   Bouaké,    'Yes');")

conn.execute("INSERT INTO Player VALUES (5, 'Cole Palmer',      'UK',   Wythenshawe,    'Yes');")

conn.execute("INSERT INTO Player (Player_Id, Player_Name, Country) VALUES (6,'Antonie Greizmann',   'France');")

conn.commit()
print("Rows inserted successfully!")

Players = pd.read_sql("SELECT * FROM Player;", conn)
print(Players)

#---PART 3: PRIMARY KEY in Action ---0
# PRIMARY KEY uniquely identifies every row.
# No two rows can share the same city_Id.#
# The column alsocnnot ne NULL.
#Trying to insert a duplicate PRIMARY KEY raises an error

print("\n-- Testing PRIMARY KEY --")
try:
    conn.excute("INSERT INTO City VALUES (1, 'Antonie semeyo', 'UK', Manchester city, 'Yes');")
    conn.commit()
except Exception as e:
    conn.rollback()
    print("Rejected:", e)
    print("Player_Id 1 already belongs to Victor Oshimen -- PRIMARY KEY must be unique.")

# --- PART 4: NOT NULL and UNIQUE in Action ---

print("\n--- Testing NOT NULL ---")
try:
    conn.execute("INSERT INTO Player VALUES (7, '', NULL, 3645000, 'Yes');")
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