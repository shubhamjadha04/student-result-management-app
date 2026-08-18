import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'shubham2004',
    database = 'student_db'
)

conn.commit()
conn.close()

print("connected successfully...")