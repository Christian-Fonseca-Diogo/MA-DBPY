import csv
import mysql.connector

# Connexion à la base de données
conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="CmonrienDiogre#+",
    database="db_reminder"
)
cursor = conn.cursor()

# Lecture du CSV et insertion dans la table
with open('classes.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    for row in reader:
        cursor.execute(
            "INSERT INTO classes (nom, salle) VALUES (%s, %s)",
            (row['Nom'], row['Salle'])
        )

conn.commit()
cursor.close()
conn.close()
print("Données insérées avec succès !")