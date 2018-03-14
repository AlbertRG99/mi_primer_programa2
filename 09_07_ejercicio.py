# Un programa que encuentre el número más pequeño de una lista dada por el usuario.

numeros_usuario = []
numero_usuario = ""

while len(numeros_usuario) < 10:
    while not numero_usuario.isdigit():
        numero_usuario = input("Dimne un número: ")
    numeros_usuario.append(numero_usuario)
    numero_usuario = ""
    print("número añadido")

numero_menor = numeros_usuario[0]
for numero in numeros_usuario:
    if numero < numero_menor:
        numero_menor = numero

print(numero_menor)