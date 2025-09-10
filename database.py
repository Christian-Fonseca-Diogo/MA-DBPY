import mysql.connector



def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="ton_user",
        password="ton_password",
        database="ta_base"
    )

def get_students():
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM eleves ORDER BY nom")
    results = cursor.fetchall()
    cursor.close()
    db.close()
    return results

# Autres fonctions: ajouter, supprimer élève, etc.