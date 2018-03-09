# Crea un programa que te cuente los espacios, puntos y comas en una frase introducida por el usuario.

frase_usuario = input("Intropduce una frase: ")

puntos = "."
punto = 0
comas = ","
coma = 0
espacios = " "
espacio = 0
for signos in frase_usuario:
    if signos == puntos:
        punto += 1
    if signos == comas:
        coma +=1
    if signos == espacios:
        espacio += 1

print("La frase tiene {} comas, {} puntos y {} espacios".format(coma, punto, espacio))

