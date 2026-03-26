import sqlite3
import csv
import os

# File names
DB_NAME = 'python_course/Examples/Sql_lite/db_example/Store.db'
CSV_FILE = 'python_course/Examples/Sql_lite/db_example/Products.csv'

# --- 0. PREPARATION: Create a fake CSV file for the example ---
# In a real case, you would already have this file.
def create_fake_csv():
    data = [
        ["Product Name", "Category", "Price", "Quantity"], # Header
        ["Gaming Laptop", "Electronics", "1200.50", "5"],
        ["Wireless Mouse", "Electronics", "25.99", "50"],
        ["Office Chair", "Furniture", "150.00", "12"],
        ["Coffee Beans", "Grocery", "18.90", "100"],
        ["4K Monitor", "Electronics", "399.99", "7"]
    ]
    with open(CSV_FILE, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(data)
    print(f"File '{CSV_FILE}' created for testing.")

# --- 1. FUNCTION TO IMPORT CSV INTO DB ---
def import_csv_to_db():
    print("\n--- Start CSV -> SQLite Import ---")
    
    # DB connection
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # 1. Create the table (if it doesn't exist)
    # Note: We define correct types (REAL for prices, INTEGER for quantities)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        category TEXT,
        price REAL,
        quantity INTEGER
    );
    """)

    # 2. Open and Read the CSV
    with open(CSV_FILE, mode='r', encoding='utf-8') as f:
        csv_reader = csv.reader(f)
        
        # IMPORTANT: Skip the CSV header
        # next() reads the first line and moves the cursor to the second
        header = next(csv_reader) 
        print(f"Header detected: {header}")

        # 3. Data preparation (TRANSFORM)
        # The CSV reads everything as strings. We need to convert the numbers.
        data_to_insert = []
        for row in csv_reader:
            # row is like ['Laptop', 'Electronics', '1200.50', '5']
            name = row[0]
            category = row[1]
            try:
                # Convert string '1200.50' -> float 1200.50
                price = float(row[2]) 
                # Convert string '5' -> int 5
                quantity = int(row[3]) 
                
                # Add the clean tuple to the list
                data_to_insert.append((name, category, price, quantity))
            except ValueError:
                print(f"Skipped corrupted row: {row}")

        # 4. Bulk insertion (LOAD)
        # Use executemany for maximum speed
        sql = "INSERT INTO products (name, category, price, quantity) VALUES (?, ?, ?, ?)"
        cursor.executemany(sql, data_to_insert)
        
        conn.commit()
        print(f"Successfully imported {cursor.rowcount} products.")

    conn.close()

# --- 2. FUNCTION TO READ FROM DB ---
def read_from_db():
    print("\n--- Reading data from SQLite ---")
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row # To access data by column name
    cursor = conn.cursor()

    # Example: Select only electronics over 300 euros
    print("Query: Looking for Electronics > 300€")
    cursor.execute("""
        SELECT name, price, quantity 
        FROM products 
        WHERE category = 'Electronics' AND price > ?
    """, (300,))

    rows = cursor.fetchall()
    
    if not rows:
        print("No products found.")
    else:
        print(f"{'PRODUCT':<20} | {'PRICE':<10} | {'AVAILABLE':<10}")
        print("-" * 45)
        for row in rows:
            # Here the data are already in the correct type (float/int), not strings!
            print(f"{row['name']:<20} | {row['price']:<10.2f} | {row['quantity']:<10}")

    conn.close()

# --- EXECUTION ---
if __name__ == "__main__":
    create_fake_csv()      # Generate the file
    import_csv_to_db()   # Write to the DB
    read_from_db()        # Read from the DB