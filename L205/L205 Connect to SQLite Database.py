import sqlite3
import pandas as pd

conn = sqlite3.connect(r"C:\Users\famil\Desktop\Darasimi-Coding-text-new-laptop\L205\L205-database.sqlite")

print("Opened data successfully")

tables = pd.read_sql("SELECT * FROM sqlite_master WHERE type='table';", conn)
print(tables)