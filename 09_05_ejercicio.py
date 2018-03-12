#Haz una tavla de multiplicar que sólo muestre los múltiplos dfe dos.

numero_usuario = int(input("Introduce un número: "))

for a in range(1,11):
    b = a % 2
    if b == 0:
       print("{} X {} = {}".format(numero_usuario, a, numero_usuario * a))





