
texto_usuario = input("Introduce un texto: ")

vocales = ["a", "e", "i", "o", "u",]

vocal = []

for letra in texto_usuario:
    if letra in vocales:
        vocal.append(letra)

print(vocal)

