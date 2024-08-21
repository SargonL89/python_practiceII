# Le pida al usuario algún texto.
# Compruebe si el texto introducido es un palíndromo e imprima el resultado.
# Supón que una cadena vacía no es un palíndromo.
# Trata a las letras mayúsculas y minúsculas como iguales.
# Los espacios no se toman en cuenta durante la verificación: trátalos como inexistentes.

def main():
    text = input("Ingresa un texto: ").lower().replace(" ", "")
    print(verifier(text))

def verifier(text):
    if text == text[::-1] and not text == "":
        return("Es un palíndromo")
    else:
        return("No es un palíndromo")

main()


    # for ch in text:
    #     if ch == text[rch:rchf]:
    #         print(text[rch:rchf])
    #         rch -= 1
    #         # rchf = int(rchf)
    #         rchf -= 1
    #         print("True")
    #     else:
    #         print("False")
    #         print(text[rch:rchf])
    # return ("Terminado")

    




    # text_eval = text
    # for _ in range(len(text)):

    #     if text_eval.endswith(ch):
    #         text_eval = text_eval.removesuffix()
    #     if texto.find(ch) == texto.rfind(ch):
    #         verified = True
    #         print(verified)
    #     else:
    #         verified = False
    #         print(verified)