import sqlite3

# database connection
conn = sqlite3.connect('python_course/Examples/Sql_lite/db_example/example.db')
cur = conn.cursor()

# query with filter
cur.execute("SELECT name, grade FROM students WHERE grade > ?", (25, ))

# retrieve results
honors_students = cur.fetchall()

# print the results
for name, grade in honors_students:
    print(f"{name} got {grade}")
    
# close connection
conn.close()