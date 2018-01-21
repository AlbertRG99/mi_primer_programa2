numero_a_adivinar = int(input("Número a adivinar (Que tu compañaro no lo vea): "))

intento = int(input("Afivina un número del uno 1 al 10: "))

if numero_a_adivinar == intento:
    print("Has ganado")
else:

    while numero_a_adivinar != intento:

        intento = int(input("Afivina un número del uno 1 al 10: "))

        if numero_a_adivinar == intento:
            print("Has ganado¡")
