from sys import argv, exit
from os import path

def main():
    check_argsnumber(argv)
    check_filestype(argv[1], argv[2])


def check_argsnumber(arguments):
    if len(arguments) != 3:
        if len(arguments) < 3:
            exit("Too few command-line arguments")
        else:
            exit("Too many command-line arguments")

def check_filestype(arg_1, arg_2):
    try:
        if not path.exists(arg_1):
            exit("Input does not exist")

        op, opf = arg_2.lower().split(".")
        ip, ipf = arg_1.lower().split(".")

        if opf not in ["JPEG", "PNG"]:
            exit("Invalid output")

        if ipf != opf:
            exit("Input and output have different extensions")

    except Exception as e:
        print(f"Error: {e}")



if __name__ == "__main__":
    main()