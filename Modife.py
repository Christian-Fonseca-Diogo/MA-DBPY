import mysql.connector
import os
from dotenv import load_dotenv

# Charger le fichier .env
load_dotenv("passwordc.env")

# Configuration MySQL
config = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME")
}

# Connexion à la base
connexion = mysql.connector.connect(**config)
curseur = connexion.cursor()

print("=== Menu Base de Données ===")
print("1 - Mettre à jour un attribut")
print("2 - Afficher les enregistrements")
choix = input("➡ Entrez votre choix (1 ou 2) : ").strip()

if choix == "2":
    # Afficher tous les enregistrements d'une table
    table = input("Nom de la table à afficher : ").strip()
    try:
        curseur.execute(f"SELECT * FROM {table}")
        lignes = curseur.fetchall()
        colonnes = [desc[0] for desc in curseur.description]

        print(f"\n📋 Contenu de la table '{table}' :")
        print(" | ".join(colonnes))
        print("-" * 50)
        for ligne in lignes:
            print(" | ".join(str(x) for x in ligne))
        print()
    except mysql.connector.Error as err:
        print("❌ Erreur :", err)

elif choix == "1":
    # Mise à jour d'un attribut
    table = input("Nom de la table : ").strip()
    colonne = input("Nom de la colonne à modifier : ").strip()
    nouvelle_valeur = input("Nouvelle valeur : ").strip()
    condition_colonne = input("Nom de la colonne pour la condition (ex: id, nom) : ").strip()
    condition_valeur = input("Valeur de la condition : ").strip()

    try:
        requete = f"UPDATE {table} SET {colonne} = %s WHERE {condition_colonne} = %s"
        curseur.execute(requete, (nouvelle_valeur, condition_valeur))
        connexion.commit()

        if curseur.rowcount > 0:
            print(f"✅ {curseur.rowcount} enregistrement(s) mis à jour avec succès !")
        else:
            print("ℹ️ Aucun enregistrement correspondant trouvé.")
    except mysql.connector.Error as err:
        print("❌ Erreur lors de la mise à jour :", err)

else:
    print("⚠️ Choix invalide. Relance le programme et choisis 1 ou 2.")

# Fermeture
curseur.close()
connexion.close()
print("\n🔒 Connexion fermée.")
