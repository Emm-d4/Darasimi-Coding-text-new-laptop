#---- PART 1: Open the Databsase
# This databse stores information about popular movies
# It has three tables: Movie, Actor, and Movie_Actor.

import sqlite3
import pandas as pd

conn = sqlite3.connect(r"C:\Users\famil\Desktop\Darasimi-Coding-text-new-laptop\L207\movies.db")

print('Opened data successfully')

# --- PART 2: DISTINCT -- Unique Values Only ---
# DISTINCT removes duplicate values -- only one copy of each unique value is returned

# ALL unique genres in the Movie table
genres = pd.read_sql("""SELECT DISTINCT(Genre) 
    FROM Movie;""", conn)
print(genres)

#ALL unique countries the actors came from
countries = pd.read_sql("""SELECT DISTINCT(Country) 
    FROM Actor;""", conn)
print(countries)

# --- PART 3: ORDER BY -- Sorting Results ---
# ORDER BY SORTS THE RESULT BY A CHOSEN COLUMN.
# DEFAULT ORDER IS ASCENDING - SMALLEST OR EARLIEST FRIST.
# ADD DESC to flip it --largest or latest first.

# All movies sorted by rating -- highest rated first
top_movies = pd.read_sql("""SELECT Title, Genre, Rating 
    FROM Movie 
    ORDER BY Rating DESC;""", conn)
print(top_movies)

# All movies sorted by a year --  oldest first
oldest_first = pd.read_sql("""SELECT Title, Year 
    FROM Movie 
    ORDER BY Year;""", conn)
print(oldest_first)

# Actors sorted by birth_year -- youngest first
youngest_actors = pd.read_sql("""SELECT Actor_name, Birth_year, 
Country
    FROM Actor 
    ORDER BY Birth_Year DESC;""", conn)
print(youngest_actors)

conn.close()