#---- PART 1: Open the Databsase
# This databse stores information about popular animals
# It has three tables: Animal, Origgen, and Place to live.

import sqlite3
import pandas as pd

conn = sqlite3.connect(r"C:\Users\famil\Desktop\Darasimi-Coding-text-new-laptop\L207\animal.db")

print('Opened data successfully')

# --- PART 2: DISTINCT -- Unique Values Only ---
# DISTINCT removes duplicate values -- only one copy of each unique value is returned

# ALL unique genres in the animal table
genres = pd.read_sql("""SELECT DISTINCT(Genre) 
    FROM Animal;""", conn)
print(genres)

#ALL unique countries the animal came from
countries = pd.read_sql("""SELECT DISTINCT(Country) 
    FROM animal;""", conn)
print(countries)

# --- PART 3: ORDER BY -- Sorting Results ---
# ORDER BY SORTS THE RESULT BY A CHOSEN COLUMN.
# DEFAULT ORDER IS ASCENDING - SMALLEST OR EARLIEST FRIST.
# ADD DESC to flip it --largest or latest first.

# All animal sorted by rating -- highest rated first
top_animal = pd.read_sql("""SELECT Title, Genre, Rating 
    FROM animal 
    ORDER BY Rating DESC;""", conn)
print(top_animal)

# All animal sorted by a year --  oldest first
oldest_first = pd.read_sql("""SELECT Title, Year 
    FROM animal 
    ORDER BY Year;""", conn)
print(oldest_first)

# animal sorted by birth_year -- youngest first
youngest_Animals = pd.read_sql("""SELECT Animal_name, Birth_year, 
Country
    FROM Animal 
    ORDER BY Birth_Year DESC;""", conn)
print(youngest_Animals)

conn.close()