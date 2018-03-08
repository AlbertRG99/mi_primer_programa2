#definimos una lista vacia
mi_lista = []

#"input_usuario" lo definimos a una string vacia

input_usario = input("¿Qué necesitas comprar? (Eccribe FIN para terminar):")

while input_usario != "FIN":
    mi_lista.append(input_usario)
    input_usario = input("¿Qué necesitas comprar? (Eccribe FIN para terminar):")

#Con for recorremos la lista.

for item in mi_lista:
    print("tengo que comprar {}".format(item))

print("Esta es mi lista de la compra")
