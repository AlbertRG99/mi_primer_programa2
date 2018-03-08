mi_lista = ["Lechuga", "Tomate", "Helado", "Pan", "Pasta", "Olivas", "Atún", "Fanta"]

#Pare ver el largo usamos len.

print(len(mi_lista))

largo_lista = len(mi_lista)
indice_actual = 0

while indice_actual < largo_lista:
    print("Tengo que comprar {}".format(mi_lista[indice_actual]))
    indice_actual += 1

print("Esta es la lista de la compra")

#Para añadir elementos a la listas se utiliza el método ".append"

mi_lista.append("Pimientos")

print(mi_lista)




