import mysql.connector as connector
import csv
import os

# -----------------------------
# FILE PATH (THIS FIXES ERROR)
# -----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, "student_data.csv")

print("Looking for CSV at:", CSV_PATH)

# -----------------------------
# MYSQL CONNECTION
# -----------------------------
conn = connector.connect(
    host="localhost",
    user="root",
    password="765180",
    port=3306
)

cursor = conn.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS college_db")
cursor.execute("USE college_db")

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    gender VARCHAR(10),
    email VARCHAR(100) UNIQUE,
    course VARCHAR(50)
)
""")

insert_query = """
INSERT INTO students
(name, age, gender, email, course)
VALUES (%s, %s, %s, %s, %s)
"""

data = []

with open(CSV_PATH, mode="r", encoding="utf-8") as file:
    csv_reader = csv.reader(file)
    next(csv_reader)

    for row in csv_reader:
        if len(row) == 5:
            data.append(tuple(row))

cursor.executemany(insert_query, data)
conn.commit()


cursor.execute("SELECT * FROM students")
print(cursor.fetchall())

cursor.close()
conn.close()
