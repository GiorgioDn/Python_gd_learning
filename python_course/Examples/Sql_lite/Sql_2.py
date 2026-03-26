import sqlite3
import os

# Database file name
db_filename = 'python_course/Examples/Sql_lite/db_example/Library.db'

# Remove the file if it already exists to have a clean environment for each execution
if os.path.exists(db_filename):
    os.remove(db_filename)

# 1. CREATION AND CONNECTION
# If the file does not exist, it is created. If it exists, it is opened.
print(f"--- Connection to {db_filename} ---")
conn = sqlite3.connect(db_filename)

# 2. CURSOR CREATION
# The cursor is the "operational arm" of the connection
cursor = conn.cursor()

# 3. TABLE CREATION (DDL)
# We use triple quotes to write SQL on multiple lines cleanly
sql_create_table = """
CREATE TABLE IF NOT EXISTS books (
id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT NOT NULL,
author TEXT NOT NULL,
year INTEGER,
price REAL
);
"""
cursor.execute(sql_create_table)
print("Table 'books' created successfully.")

# 4. DATA INSERTION (INSERT) - Single Method
# NOTE: Use '?' as a placeholder for security (avoids SQL Injection)
sql_insert = "INSERT INTO books (title, author, year, price) VALUES (?, ?, ?, ?)"
book_data = ("The Lord of the Rings", "J.R.R. Tolkien", 1954, 25.50)

cursor.execute(sql_insert, book_data)
print("Inserted a single book.")
# commit the changes
conn.commit()

# 5. MULTIPLE INSERTION (executemany) - Much faster for large amounts of data
book_list = [
    ("1984", "George Orwell", 1949, 12.00),
    ("The Little Prince", "Antoine de Saint-Exupéry", 1943, 9.50),
    ("Dune", "Frank Herbert", 1965, 18.90),
    ("Python Crash Course", "Eric Matthes", 2019, 35.00)
]

cursor.executemany(sql_insert, book_list)
print(f"Inserted {cursor.rowcount} books in bulk.")

# 6. SAVING (COMMIT)
# Fundamental! Without this, the data would be lost upon closing.
conn.commit()
print("Changes committed (saved) to the DB.")

# 7. READING DATA (SELECT)
print("\n--- Reading all books ---")
cursor.execute("SELECT * FROM books")

# fetchall() retrieves all remaining rows as a list of tuples
all_books = cursor.fetchall()

for book in all_books:
# book is a tuple: (id, title, author, year, price)
    print(f"ID: {book[0]} | Title: {book[1]} | Price: {book[4]}€")
    
# 8. FILTERED READING AND UPDATE (UPDATE)
print("\n--- Price Update for Orwell ---")
# Search for the ID of 1984
cursor.execute("SELECT id FROM books WHERE author = ?", ("George Orwell",))
id_orwell = cursor.fetchone()[0] # fetchone returns a single tuple or None

# Update the price
new_price = 15.00
cursor.execute("UPDATE books SET price = ? WHERE id = ?", (new_price, id_orwell))
conn.commit()
print(f"Price updated for ID {id_orwell}.")

# 9. DELETION (DELETE)
print("\n--- Deleting old books ---")
cursor.execute("DELETE FROM books WHERE year < ?", (1950,))
print(f"Deleted {cursor.rowcount} books published before 1950.")
conn.commit()

# 10. CONNECTION CLOSURE
# Releases the file resources
conn.close()
print("\nConnection closed.")