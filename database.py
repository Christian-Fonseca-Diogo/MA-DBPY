import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv("passwordc.env")

def open_db():
    return mysql.connector.connect(host=os.getenv('DB_HOST', '127.0.0.1'), port=os.getenv('DB_PORT', '3306'),
                                   user=os.getenv('DB_USER'), password=os.getenv('DB_PASSWORD'), database=os.getenv('DB_NAME'),
                                   buffered=True, autocommit=True)

db_connection = open_db()

def get_class_id_from_name(name):
    query = "SELECT id FROM classes WHERE name = %s"
    cursor = db_connection.cursor()
    cursor.execute(query, (name,))
    if cursor.rowcount == 0:
        cursor.close()
        return None
    else:
        row = cursor.fetchone()
        cursor.close()
        return row[0]

def add_class(name, salle):
    query = "INSERT INTO classes (name, salle) values (%s, %s)"
    cursor = db_connection.cursor()
    cursor.execute(query, (name, salle))
    inserted_id = cursor.lastrowid
    cursor.close()
    return inserted_id

def add_student(firstname, lastname, class_id):
    query = "INSERT INTO students (firstname, lastname, class_id) values (%s, %s, %s)"
    cursor = db_connection.cursor()
    cursor.execute(query, (firstname, lastname, class_id))
    inserted_id = cursor.lastrowid
    cursor.close()
    return inserted_id
