# Tu tarea es escribir un programa que:
# Le pida al usuario dos textos por separado.
# Compruebe si los textos ingresados son anagramas e imprima el resultado.
# Nota:
# Supongamos que dos cadenas vacías no son anagramas.
# Tratar a las letras mayúsculas y minúsculas como iguales.
# Los espacios no se toman en cuenta durante la verificación: trátalos como inexistentes.


import math
import random

import nltk
from nltk.corpus import words

nltk.download("words")

def main():
    while True:
        try:
            text = input("Ingrese el primer texto: ").lower()
            text = ''.join(filter(str.isalnum, text))
            n_com = number_combinations(text)
            words_list = combinations_kreator(text, n_com)
            print(verifier(words_list))

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

def combinations_kreator(word, n_com):
    combinations = []
    combinations.append(word)
    char_list = list(word)
    while len(combinations) < n_com:
        random.shuffle(char_list)
        new_word = "".join(char_list)
        if new_word not in combinations:
            combinations.append(new_word)
        else:
            continue
    return combinations

def verifier(words_list):
    counter = 0
    for w in words_list:
        if w in words.words():
            counter += 1
        if counter > 1:
            return (f"It's an anagram: {w}")
    if counter <= 1:    
        return ("It's not an anagram")

main()