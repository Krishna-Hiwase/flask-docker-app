from db import get_db_connection

conn = get_db_connection()
cursor = conn.cursor()

cursor.execute(
    "INSERT INTO users (name) VALUES (%s)",
    ("Krishna",)
)

conn.commit()

print("User inserted successfully!")

cursor.close()
conn.close()
