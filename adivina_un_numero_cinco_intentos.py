
number_to_guess = 6

user_number = int(input("Adivina un numero: "))

if user_number == number_to_guess:
    print("Has ganado")
else:
    print("Fallaste, te quedan cuatro intentos")
    user_number = int(input("Adivina un numero: "))
    if user_number == number_to_guess:
        print("Has ganado")
    else:
        print("Fallaste, te quedan tres intentos")
        user_number = int(input("Adivina un numero: "))
        if user_number == number_to_guess:
            print("Has ganado")
        else:
            print("Fallaste, te quedan dos intentos")
            user_number = int(input("Adivina un numero:"))
            if user_number == number_to_guess:
                print("Has ganado")
            else:
                print("Este es tu ultimo intento")
                user_number = int(input("Adivina un numero: "))
                if user_number == number_to_guess:
                    print("Has ganado")
                else:
                    print("Has perdido")


