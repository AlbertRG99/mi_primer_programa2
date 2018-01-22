

texto_usuario = input("Introduces un texto: ")

espacios = [" "]

puntos = ["."]

comas = [","]

n_espacios = 0

n_puntos = 0

n_comas = 0

for signo in texto_usuario:
    if signo in espacios:
        n_espacios += 1

for signo in texto_usuario:
    if signo in puntos:
        n_puntos += 1

for signo in texto_usuario:
    if signo in comas:
        n_comas += 1


print("{} espacios".format(n_espacios))

print("{} puntos".format(n_puntos))

print("{} comas".format(n_comas))












