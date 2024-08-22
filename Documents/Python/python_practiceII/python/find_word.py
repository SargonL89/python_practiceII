# Vamos a jugar un juego. Te daremos dos cadenas: una es una palabra (por ejemplo, "dog") y la segunda es una combinación de un grupo de caracteres.
# Tu tarea es escribir un programa que responda la siguiente pregunta: ¿Los caracteres que comprenden la primera cadena están ocultos dentro de la segunda cadena?
# Por ejemplo:
# Si la segunda cadena es "vcxzxduybfdsobywuefgas", la respuesta es si;
# Si la segunda cadena es "vcxzxdcybfdstbywuefsas", la respuesta es no (ya que no están las letras "d", "o", o "g" ni en ese orden)

def main():
    while True:
        try:
            string_1 = input("Ingresa un string: ").replace(" ", "").lower()
            string_2 = input("Ingresa un segundo string: ").replace(" ", "").lower()
            indice = 0
            for ch in string_1:
                indice = string_2[indice:].find(ch)
                if indice != -1:
                    resultado = True
                else:
                    resultado = False
                    break
            if resultado:
                print(f"Los caracteres de {string_1} se encuentran dentro de {string_2}")
            else:
                print(f"Los caracteres de {string_1} no se encuentran dentro de {string_2}")
        except (ValueError, TypeError) as e:
            print("Error: ", e)
        except KeyboardInterrupt:
            break

main()