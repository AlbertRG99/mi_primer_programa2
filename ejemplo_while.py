

numero_inicial = 11


while numero_inicial > 0:
    numero_inicial -= 1
    print(numero_inicial)
    if numero_inicial % 2 == 0:
        print("Este número es par")
    else:
        print("Este número es impar")

print("He terminado")