from db import get_db_connection


conn = get_db_connection()
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL
)
""")
conn.commit()

print("table created successfully!")

cursor.close()
conn.close()
