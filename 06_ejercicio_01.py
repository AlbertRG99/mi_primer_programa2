#Crea una calculadora quie le pregunte al usuario que operación quiere hacer
#  a la vez que dos númeroa con los que operar.



operacion = input("¿Que operacioón quieres realizar? (multiplicar / sumar / restar / dividir")
primer = int(input("Dime el primer número:"))
segundo = int(input("Dime el segundo número: "))

if operacion == "multiplicar":
    resultado = primer * segundo
    print("La multiplicacioón de {} y {} es igual a {}".format(primer, segundo, resultado))
if operacion == "dividir":
    resultado = primer / segundo
    print("La division de {} entre {} es igual a {}".format(primer, segundo, resultado))
if operacion == "sumar":
    resultado = primer + segundo
    print("La suma de {} y {} es igual a {}".format(primer, segundo, resultado))
if operacion == "restar":
    resultado = primer - segundo
    print("la restas de {} menos {} es igual a {}".format(primer, segundo, resultado))


