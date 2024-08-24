# from sys import path
# import os

# path.append('..\\module')
# # Alternative: path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'module')))

# import module

# zeroes = [0 for i in range(5)]
# ones = [1 for i in range(5)]
# print(module.suml(zeroes))
# print(module.prodl(ones))

def check_range(value, min_value, max_value):
    if not (min_value <= value <= max_value):
        raise ValueError(f"El valor {value} no está dentro del rango permitido ({min_value}..{max_value})")

try:
    num = int(input("Ingresa un número entre 1 y 100: "))
    check_range(num, 1, 100)
    print("El número está dentro del rango.")
except ValueError as e:
    print(e)

def chekin():
    if "Mike" > "Mikey":
        print(True)
    else:
        print(False)

chekin()

def excp():
    x = '\''
    print(len(x))

excp()