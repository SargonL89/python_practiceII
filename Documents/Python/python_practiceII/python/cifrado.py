# El cifrado César original cambia cada carácter por otro a se convierte en b, z se convierte en a, y así sucesivamente. Hagámoslo un poco más difícil y permitamos que el valor desplazado provenga del rango 1..25.
# Además, dejemos que el código conserve las mayúsculas y minúsculas (las minúsculas permanecerán en minúsculas) y todos los caracteres no alfabéticos deben permanecer intactos.
# Le pida al usuario una línea de texto para encriptar.
# Le pida al usuario un valor de cambio (un número entero del rango 1..25, nota: debes obligar al usuario a ingresar un valor de cambio válido (¡no te rindas y no dejes que los datos incorrectos te engañen!).
# Imprime el texto codificado.

def main():
    while True:
        try:
            text = input("Ingresa un mensaje a encriptar: ")
            change = int(input("Ingresa un valor de cambio: "))
            if not 1 <= change <= 25:
                print("Ingresa un valor de cambio válido entre 1 y 25!")
                continue
            print(cifrado(text, change))
        except (ValueError, TypeError) as e:
            print("Error: ", e)
            continue
        except KeyboardInterrupt:
            print("\nPrograma terminado.")
            break

def cifrado(text, change):
    cipher = ""
    for ch in text:
        if ch.isalpha():
            offset = ord('A') if ch.isupper() else ord('a')
            # El operador módulo (%) se usa para "envolver" el valor resultante si supera 25 (que es la posición de 'Z' para mayúsculas o 'z' para minúsculas). Esto asegura que la rotación continúe desde el principio del alfabeto si es necesario.
            # Por ejemplo, si el cálculo anterior da 28, entonces 28 % 26 resulta en 2, que corresponde a la tercera letra en el alfabeto, después de completar el ciclo.
            cipher += chr((ord(ch) - offset + change) % 26 + offset)
        else:
            cipher += ch
    return cipher


main()