import mysql.connector as connector
"""
Imports MySQL Connector/Python
This library speaks the MySQL client protocol over TCP
It handles:
authentication
packet framing
result parsing

"""

conn = connector.connect(
    host="localhost",
    user="root",
    password="765180",
    port=3306
)
"""
What happens internally
Python opens a TCP socket to localhost:3306
MySQL handshake occurs
User authentication (root)
Session is created on the server

Parameters  explanation
Parameter	Meaning
host	    MySQL server address (localhost = same machine)
user     	MySQL username
password	Password for the user
port	    MySQL default port (3306)
Notes

No database specified → connection is made to the server, not a specific DB
Useful for admin tasks like SHOW DATABASES
"""


print("Connected:", conn.is_connected())
"""
Purpose
Verifies whether the connection is alive and usable

If False
Connection object exists
Server is unreachable or session failed
"""

cursor = conn.cursor()
"""
What is a cursor?

A cursor is used to execute SQL queries
You cannot execute SQL directly on the connection

Analogy
conn → phone line
cursor → person speaking

Internally
Allocates server-side resources
Prepares MySQL to send query results
"""

cursor.execute('show databases')
"""
What this does
Sends SQL command to MySQL server
Server executes it
Result is stored temporarily on the server
Cursor points to the result set

Query type
DDL / Metadata query
Read-only
"""

print(cursor.fetchall())

cursor.execute("CREATE DATABASE IF NOT EXISTS school_db")
cursor.execute("USE school_db")
cursor.execute("""
CREATE TABLE IF NOT EXISTS student_details (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT CHECK (age >= 0),
    gender VARCHAR(10),
    email VARCHAR(100) UNIQUE,
    course VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

insert_query = """
INSERT INTO student_details
(name, age, gender, email, course)
VALUES (%s, %s, %s, %s, %s)
"""

students = [
    ("Aman Verma", 21, "Male", "aman@gmail.com", "AI"),
    ("Neha Singh", 23, "Female", "neha@gmail.com", "Web Development"),
    ("Riya Patel", 22, "Female", "riya@gmail.com", "Data Science")
]

cursor.executemany(insert_query, students)
conn.commit()


data = ("Rahul Sharma", 22, "Male", "rahul@gmail.com", "Data Science")

cursor.execute(insert_query, data)
conn.commit()



"""
fetchall() behavior
Fetches all remaining rows
Returns a list of tuples
"""
cursor.close()
"""
Why this is important
Frees server-side resources
Prevents cursor leaks
MySQL limits number of open cursors
Best Practice
Always close the cursor after use
"""
conn.close()
"""
Why this is important

Frees server-side resources
Prevents cursor leaks
MySQL limits number of open cursors

Best Practice
Always close the cursor after use
"""
