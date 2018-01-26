
numero_de_usuario = int(input("¿Qué número quieres muyltiplicar?: "))


for multiplicador in range(0, 11):
    if(multiplicador %2==0):
        print("{} x {} = {}".format(numero_de_usuario, multiplicador, numero_de_usuario * multiplicador))

