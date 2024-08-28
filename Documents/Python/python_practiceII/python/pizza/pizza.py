import csv
from sys import argv, exit
from tabulate import tabulate


def main():
    if len(argv) == 2:
        if argv[1].endswith(".csv"):
            return make_table(argv[1])
        else:
            exit("Not a CSV file")
    elif len(argv) < 2:
        exit("Too few command-line arguments")
    else:
        exit("Too many command-line arguments")

def make_table(file_name):
    try:
        with open(file_name, "r") as file:
            reader = csv.reader(file)
            headers = next(reader)
            table = []
            for row in reader:
                table.append(row)
            return (tabulate(table, headers, tablefmt="grid"))
    except FileNotFoundError:
        exit("File does not exist")

print(main())