# El usuario va a poder meter cosas en la list ade la compra hast aque diga "FIN".

lista = []
input_usuario = input("¿Qué necesitas comprar? (Escribe FIN para salir: ")

while input_usuario != "FIN":
    lista.append(input_usuario)
    input_usuario = input("¿Qué necesitas comprar? (Escribe FIN para salir: ")


largo_lista = len(lista)
print("Mi lista de la compra tiene {} productos".format(largo_lista))

indice_actual = 0

while indice_actual < largo_lista:
    print("Tengo que comprar: {}".format(lista[indice_actual]))
    indice_actual += 1

print("Esta es mi lista de la compra.")






