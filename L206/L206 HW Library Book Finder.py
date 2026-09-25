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

# Check book id of all books
books = pd.read_sql("""SELECT * 
                        FROM books;""", conn)
print(books)
print()

# Check date to return book
book_id = pd.read_sql("""SELECT * 
                        FROM book;""", conn)

"""**Conclusion -**

- 12 Numeric features (Integer and Numeric) and 1 categorical feature (Text)
- 3 columns with null values
"""

print(books)
print()

# Check details of all the books borrowed
book_id = pd.read_sql("""SELECT * 
                        FROM book 
                        WHERE return book == 7;""", conn)
print(book_id)
print()

# Check details of all the books returned in the last 2 years
date_returned = pd.read_sql("""SELECT * 
                        FROM book 
                        WHERE Date_Returned == 7 and Date_Id IN (8,9);""", conn)
print(date_returned)
print()

books_read = pd.read_sql("""SELECT * 
                        FROM book 
                        WHERE books_read LIKE 'De%';""", conn)
print(books_read)
print()