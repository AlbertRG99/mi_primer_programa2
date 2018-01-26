numeros_usuario = []

numero_del_usuario = ""

while len(numeros_usuario) < 6:
    while not numero_del_usuario.isdigit():
        numero_del_usuario = input("Dime un número: ")
    numeros_usuario.append(int(numero_del_usuario))
    numero_del_usuario = ""
    print("Número añadido")



print("Los números que has introducido son: {} ".format(numeros_usuario))

numero_peque = numeros_usuario[0]

for numero in numeros_usuario:
    if numero < numero_peque:
        numero_peque = numero


print("El largo de la lista es de: {}".format(numero_peque))