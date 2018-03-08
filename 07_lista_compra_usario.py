
#definimos una lista vacia
mi_lista = []

#"input_usuario" lo definimos a una string vacia

input_usario = input("¿Qué necesitas comprar? (Eccribe FIN para terminar):")

while input_usario != "FIN":
    mi_lista.append(input_usario)
    input_usario = input("¿Qué necesitas comprar? (Eccribe FIN para terminar):")

largo_lista = len(mi_lista)
imdice_actual = 0

while largo_lista > imdice_actual:
    print("Tango que comprar {}".format(mi_lista[imdice_actual]))
    imdice_actual += 1

print("Esta es mi lista de la compra")

