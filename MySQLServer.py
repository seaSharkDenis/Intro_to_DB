import mysql.connector
import os
from dotenv import load_dotenv


load_dotenv()

db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")

try:
    connection = mysql.connector.connect(
        host = db_host,
        user = db_user,
        password = db_password
    )
    if connection.is_connected():
        print("Connection Successful")

        cursor = connection.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")
    else:
        print("Connection to database failed.")
except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    if connection and connection.is_connected():
        cursor.close()
        connection.close()
