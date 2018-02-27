number_to_guest = 5

user_number = int(input("Dime un número: "))

if user_number == number_to_guest:
    print("Has acertado")
else:
    print("Has dicho {}, has fallado, te quedan 4 intentos".format(user_number))
    user_number = int(input("Dime un número"))
    if user_number == number_to_guest:
        print("Has acertado")
    else:
        print("Has dicho {}, has fallado, te quedan 3 intentos".format(user_number))
        user_number = int(input("Dime un número"))
        if user_number == number_to_guest:
            print("has acertado")
        else:
            print("Has dicho {}, has fallado, te quedan 2 intentos".format(user_number))
            user_number = int(input("Dime un número: "))
            if user_number == number_to_guest:
                print("Has acertado: ")
            else:
                print("Has dicho {}, has fallado, este es tu último intento".format(user_number))
                user_number = int(input("Dime un número: "))
                if user_number == number_to_guest:
                    print("Has acertado")
                else:
                    print("Has dicho {}, has fallado, no te quedan más intentos.".format(user_number))
