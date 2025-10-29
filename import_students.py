from database import *

with open("students.csv", encoding='latin-1') as file:
    next(file)
    for line in file:
        row = line.strip().split(";")
        class_id = get_class_id_from_name(row[3])
        if class_id:
            add_student(row[0], row[1], class_id)
        else:
            print(f"La classe {row[3]} n'existe pas pour la ligne: {row}")
