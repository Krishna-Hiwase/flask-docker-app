from db import get_db_connection

conn = get_db_connection()
cursor = conn.cursor()

cursor.execute("SELECT * FROM users")

for row in cursor.fetchall():
    print(row)

cursor.close()
conn.close()
