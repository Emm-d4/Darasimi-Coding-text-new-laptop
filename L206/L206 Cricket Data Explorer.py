import sqlite3
import pandas as pd

conn = sqlite3.connect (r"C:\Users\famil\Desktop\Darasimi-Coding-text-new-laptop\L206\database2.sqlite")

print("Opened data successfully")
print()

# Read 5QL query for getting all the tables of databse into a dataframe
tables = pd.read_sql("""SELECT * 
                    FROM sqlite_master
                    WHERE type='table';""", conn)
print(tables)
print()

# Check team id of all teams
teams = pd.read_sql("""SELECT * 
                        FROM Team;""", conn)
print(teams)
print()

# Check Macthes
macthes = pd.read_sql("""SELECT * 
                        FROM Macth;""", conn)

"""**Conclusion -**

- 12 Numeric features (Integer and Numeric) and 1 categorical feature (Text)
- 3 columns with null values
"""

print(macthes)
print()

# Check detaails of all the matches won by Mumbai Indians
MI_wins = pd.read_sql("""SELECT * 
                        FROM Match 
                        WHERE Match_Winner == 7;""", conn)
print(MI_wins)
print()

# Check details of all the macthes won by Mumbai Indians in last 2 seasons
MI_S8_S9 = pd.read_sql("""SELECT * 
                        FROM Match 
                        WHERE Macth_Winner == 7 and Season_Id IN (8,9);""", conn)
print(MI_S8_S9)
print()

new_teams = pd.read_sql("""SELECT * 
                        FROM Team 
                        WHERE Team_Name LIKE 'De%';""", conn)
print(new_teams)
print()