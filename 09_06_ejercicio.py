#Crea una tabla de multilicar invertida a partir del número del usuario.

numero_usuario = int(input("Introduce un número:"))

for a in range(10, 0, -1):
    print("{} X {} = {}".format(numero_usuario, a, numero_usuario * a))
