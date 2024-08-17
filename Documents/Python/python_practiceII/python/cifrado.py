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
            if change < 1 or change > 25:
                print("Ingresa un valor de cambio válido!")
                continue
            print(cifrado(text, change))
        except KeyboardInterrupt:
            break
        except ValueError as e:
            print("Error: ", e)
            continue
        except TypeError as e:
            print("Error: ", e)
            continue
        except:
            continue

def cifrado(text, change):
    cipher = ""
    for ch in text:
        if not ch.isalpha():
            cipher += ch
        else:
            more_than_z = ord(ch) + change
            if ch.isupper() and more_than_z > ord("Z"):
                counter_up = ord("Z") - ord(ch)
                cipher += chr(change - counter_up + ord("A") - 1)
            elif not ch.isupper() and more_than_z > ord("z"):
                counter_up = ord("z") - ord(ch)
                cipher += chr(change - counter_up + ord("a") - 1)
            else:
                cipher += chr(ord(ch) + change)
    return cipher


main()