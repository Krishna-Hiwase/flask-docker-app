import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
            host="mysql",
            user="krishna",
            password="pass123",
            database="mydb"
            
     )

