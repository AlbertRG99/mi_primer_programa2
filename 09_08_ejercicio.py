#Contar elementos de una lista de números dada por el usuario.

numeros_usuario = []

numero_usuario = ""
while not numero_usuario.isdigit():
    numero_usuario = input("Introduce un número (Escribe FIN para terminar: ")
    while numero_usuario != "FIN":
        numeros_usuario.append(numero_usuario)
        numero_usuario = input("Introduce un número (Escribe FIN para terminar: ")

print(numeros_usuario)


while not numero.isdigit() or numero != "FIN":
    numero = (input("Introduce un número (escribe FIN para terminar: "))
numeros_usuario.append(numero)




print(numeros_usuario)