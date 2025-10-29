from database import *

with open("classes.csv") as file:
    next(file)
    for line in file:
        row = line.strip().split(";")
        if get_class_id_from_name(row[0]):
            print(f"Cette classe existe déjà: {row[0]}")
        else:
            add_class(row[0], row[1])
