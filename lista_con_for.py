
# Hay una forma más eficiente de recocorrer una lista: con "for".

lista = []
input_usuario = input("¿Qué necesitas comprar? (Escribe FIN para salir: ")

while input_usuario != "FIN":
    lista.append(input_usuario)
    input_usuario = input("¿Qué necesitas comprar? (Escribe FIN para salir: ")

# Por cada item en lista
# Imprimir item

for item in lista:
    print("Tengo que comprar: {}".format(item))



print("Esta es mi lista de la compra.")


