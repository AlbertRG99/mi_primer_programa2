
# Crea un programa que cuente el número de vocales en una frase dada por el usuario.


frase_del_usuario = input("Escribe una frase: ")


vocales = ["a", "e", "i", "o", "u"]

n_vocales = 0

n_consonantes = 0

for letra in frase_del_usuario:
    if letra in vocales:
        n_vocales += 1
    else:
        n_consonantes += 1

print("La frase teine {} vocales y {} consonantes".format(n_vocales, n_consonantes))





