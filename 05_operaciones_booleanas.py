apetece_helado = input("¿Te apatece un helado? (Si No/): ").upper()
tienes_dinero = input("¿Tienes dinero para un helado? (Si No/): ").upper()
esta_tu_tia = input("¿Está tu tía? (Si/No): ").upper()
esta_el_heladero = input("¿Está el heladero? (Si/No): ").upper()

if apetece_helado == "SI" and (tienes_dinero == "SI" or esta_tu_tia == "SI") and esta_el_heladero == "SI":
   print("Cómete un helado")
else:
    print("Pues nada")


