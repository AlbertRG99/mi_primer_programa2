

# Obtener la tabla de multiplicar de un número esspecificado por el usuario.


numero_tabla = int(input("¿De qué número quieres ver la tabla de multiplicar?: "))


# En Phyton existe una forma de cojer una serie de numeros: "range"


for a in range (1, 11):
    print(a)

for multiplo in range(1, 11):
    print("{} x {} = {}".format(numero_tabla, multiplo, numero_tabla * multiplo))





