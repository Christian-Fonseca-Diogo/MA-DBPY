import random
import database


def afficher_menu():
    print("\nMenu :")
    print("1. Afficher l’ordre en classe")
    print("2. Générer le planning « Ordre en classe »")
    print("3. Valider l’ordre en classe de la semaine")
    print("4. Supprimer un élève de la liste")
    print("5. Ajouter un élève de la liste")
    print("6. Générer le document « Ordre en classe »")
    print("7. Sortir du menu")

def main():
    while True:
        afficher_menu()
        choix = input("Choisissez une option (1-7): ")

        if choix == '1':
            eleves = get_students()
            print("\nOrdre en classe:")
            for e in eleves:
                print(f"- {e[1]} {e[2]}")  # selon ta structure (ex: id, prénom, nom)
        elif choix == '7':
            print("Au revoir!")
            break
        else:
            print("Option non encore implémentée.")

if __name__ == "__main__":
    main()

