

lista = ["Lechuga", "Tomate", "Helado", "Pan", "Psta", "Oivas", "Atún", "Fanta"]

# Podemos añadir items a una lista con append

lista.append("Pimientos")

print(lista[1])

# Para saber el largo de una lista se utiliza len

largo_lista = len(lista)

print("Mi lista de la compra tiene {} productos".format(largo_lista))

# Se pueden usar índices negativos. Si ponemos -1 accedemos al último item de la lista

print("El último producto de la lista es: {}".format(lista[-1]))

print("El primer producto de la lista es: {}, el segundo es: {}, el cuarto es: {}".format(lista[0],lista[2],lista[3]))

# Podemos recorrer la lista usando un "while":

indice_actual = 0

while indice_actual < largo_lista:
    print("Tengo que comprar: {}".format(lista[indice_actual]))
    indice_actual += 1

print("Esta es mi lista de la compra.")