#Crea un programa capaz de contar mayúsculas.

frase_usuario = input("Introduce una frase: ")

may = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "Y", "Z"]

mayus = 0

for letra in frase_usuario:
    if letra in may:
        mayus += 1

print("la frase tiene {} mayúsculas".format(mayus))


