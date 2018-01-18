operacion_matametica = input("Qué operación matamática quieres realizar (multipicar / dividir / restar / sumar: ")

primer_numero = int(input("Elige el primer número: "))

segundo_numero = int(input("Elige el segundo número: "))

if operacion_matametica == "dividir":
    resultado = primer_numero / segundo_numero

elif operacion_matametica == "multiplicar":
    resultado = primer_numero * segundo_numero

elif operacion_matametica == "restar":
    resultado = primer_numero - segundo_numero

elif operacion_matametica == "sumar":
    resultado = primer_numero + segundo_numero

print("Resultado: {}".format(resultado))