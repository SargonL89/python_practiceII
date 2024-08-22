# Algunos dicen que el Dígito de la Vida es un dígito calculado usando el cumpleaños de alguien. Es simple: solo necesitas sumar todos los dígitos de la fecha. Si el resultado contiene más de un dígito, se debe repetir la suma hasta obtener exactamente un dígito. Por ejemplo:
# 1 Enero 2017 = 2017 01 01
# 2 + 0 + 1 + 7 + 0 + 1 + 0 + 1 = 12
# 1 + 2 = 3
# 3 es el dígito que buscamos y encontramos.
# Tu tarea es escribir un programa que:
# Le pregunté al usuario su cumpleaños (en el formato AAAAMMDD o AAAADMM o MMDDAAAA; en realidad, el orden de los dígitos no importa).
# Dé como salida El Dígito de la Vida para la fecha ingresada.

def main():
    while True:
        try:
            life_digit = input("Ingresa tu fecha de nacimiento: ").replace(" ", "")
            counter = 0
            while counter < 5:
                if len(life_digit) == 1:
                    print(life_digit)
                    break
                else: 
                    life_digit = calculator(life_digit)
                counter += 1
        except (ValueError, TypeError) as e:
            print("Error: ", e)
            continue
        except KeyboardInterrupt:
            break

def calculator(date):
    total = 0
    for n in date:
        n = int(n)
        total += n
    return str(total)

main()