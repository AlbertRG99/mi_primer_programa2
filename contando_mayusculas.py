
texto_usuario = input("Introduce un texto: ")

mayusculas = ["A", "B", "C", "D", "E", "F","G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "Y", "Z"]

n_mayusculas = 0

for letra in texto_usuario:
    if letra in mayusculas:
        n_mayusculas += 1

print("Mayúsculas = {}".format(n_mayusculas))






