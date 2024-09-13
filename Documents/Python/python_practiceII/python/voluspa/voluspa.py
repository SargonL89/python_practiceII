def read_voluspa():
    with open("voluspa.txt", "r") as file:
        words = file.read().split()
        print(len(words))

def write_inp_user():
    while True:
        text_user = input("Introduce un texto: ")
        if text_user == " ":
            break
        with open("entrada_usuario.txt", "a") as file:
            file.write("\n", text_user)
        
import csv

def modifying():
    students = []
    with open("students.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append({"name": row["nombre"], "lastname": row["apellido"], "age": row["edad"]})

        for student in sorted(students, key=lambda student: student["name"]):
            print(f"{student['name']} {student['lastname']} is {student['age']}")


modifying()