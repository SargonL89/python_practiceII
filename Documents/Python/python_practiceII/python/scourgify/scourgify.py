import csv
from sys import argv, exit

def main():
    if len(argv) == 3:
        csv_reader(argv[1], argv[2])
    elif len(argv) < 3:
        exit("Too few command-line arguments")
    else:
        exit("Too many command-line arguments")

def csv_reader(before, after):
    try:
        with open(before) as file:
            reader = csv.DictReader(file)
            csv_writer(reader, after)
    except Exception as e:
        print(f"Error: {e}")
        exit("Could not read invalid_file.csv")

def csv_writer(before, after):
    try:
        students = []
        for row in before:
            first_n, last_n = row["name"].split(",")
            students.append({"first": first_n, "last": last_n, "house": row["house"]})
        print(students)

        with open(after, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["first","last","house"])
            writer.writeheader()
            for student in students:
                writer.writerow({"first": student["first"], "last": student["last"].strip(), "house": student["house"]})

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()