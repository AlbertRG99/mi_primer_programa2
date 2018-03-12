""" Haz una tabla de multiplicar qiue vaya del 5 al 15 de un número dado por el usuario"""


numero_usuario = int(input("Introduce un número para obtener la tabla del 5 al 15: "))

for a in range(5, 16):
    print("{} x {} = {}".format(a, numero_usuario, a * numero_usuario))


