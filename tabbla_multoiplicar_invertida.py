
numero_usuario = int(input("¿Qué número quieres multiplicar?: "))


for multiplicardor in range(11, 0, -1):
    print("{} x {} = {}".format(numero_usuario, multiplicardor,  numero_usuario * multiplicardor))

