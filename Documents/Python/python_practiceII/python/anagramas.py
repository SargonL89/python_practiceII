# Tu tarea es escribir un programa que:
# Le pida al usuario dos textos por separado.
# Compruebe si los textos ingresados son anagramas e imprima el resultado.
# Nota:
# Supongamos que dos cadenas vacías no son anagramas.
# Tratar a las letras mayúsculas y minúsculas como iguales.
# Los espacios no se toman en cuenta durante la verificación: trátalos como inexistentes.

# factoriales para contar el número de veces que pueden combinarse las letras de una palabra en un bucle while?
# el resultado del cálculo factorial indica la cantidad de formas en las que pueden combinarse las letras, pero llegar a esas combinaciones no puede hacerse directamente con sort
# guardas en una lista la combinación que se realizó y vas exceptuando cada una de las anteriores
# bibliotecas para detectar si la palabra existe

import math
import random


def main():
    while True:
        try:
            text = input("Ingrese el primer texto: ").lower()
            text = ''.join(filter(str.isalnum, text))
            n_com = number_combinations(text)
            print(verifier(text, n_com))
        except (ValueError, TypeError) as e:
            print("Error: ", e)
            continue
        except KeyboardInterrupt:
            break

def number_combinations(word):
    num = 0
    letters = {}
    for _ in word:
        num += 1
    for i in word:
        if i not in letters:
            letters[i] = 1
        else:
            letters[i] += 1
    
    divisor = 1
    for value in letters.values():
        divisor *= math.factorial(value)
    
    n_com = int(math.factorial(num) / divisor)
    return n_com

def verifier(word, n_com):
    combinations = []
    combinations = combinations.append(word)
    char_list = list(word)
    while len(combinations) < n_com:
        new_word = "".join(random.shuffle(char_list))
        if new_word not in combinations:
            combinations.append(new_word)
        else:
            continue


main()