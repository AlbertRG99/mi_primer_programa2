# Adivina un número. Primero preguntamos el número y loego otro usuario tiene que adivinarlo.
# El programa solo termina cuando adivenme el número.

numero = int(input("Introduce el número a adivinar (Que tu compañero no lo vea): "))

numero_usuario = int(input("Adivina un número: "))

while numero != numero_usuario:
    numero_usuario = int(input("Has fallado vuelve a intentarlo: "))
print("Has acertado.")
