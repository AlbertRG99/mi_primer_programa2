# Crear un programa que muestre por pantallas la lista de todas las vocales de una frase.

frase_usuario = input("Introduce una frase:")

vocales = ["a", "e", "i", "o", "u"]

ouput = []

for letra in frase_usuario:
    if letra in vocales:
        ouput.append(letra)

print("La frase tiene las siguiente vocales {}".format(ouput))





