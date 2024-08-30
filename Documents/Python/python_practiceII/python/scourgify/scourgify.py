import csv
from sys import argv, exit

def main():
    if len(argv) != 3:
        exit("Usage: python scourgify.py before.csv after.csv")

    csv_reader(argv[1], argv[2])

def csv_reader(before, after):
    try:
        with open(before, newline='') as file:
            reader = csv.DictReader(file)
            csv_writer(reader, after)
    except Exception as e:
        print(f"Error: {e}")
        exit("Could not read {before}")

def csv_writer(reader, after):
    try:
        students = []
        for row in reader:
            last_n, first_n = row["name"].split(",")
            students.append({
                "first": first_n.strip(),
                "last": last_n.strip(),
                "house": row["house"].strip()
            })

        with open(after, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
            writer.writeheader()
            writer.writerows(students)

    except Exception as e:
        print(f"Error: {e}")
        exit("Could not write to {after}")

if __name__ == "__main__":
    main()