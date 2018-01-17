

apetece_helado_input = input("¿Te apetece un helado? (Sí / No): ").upper()
tiene_dinero_input = input("¿Tienes dinero para un helado? (Sí / No: )").upper()
esta_el_heladero_input = input("¿Está el señor heladero? (Si / No)").upper()
esta_tu_tia_input = input("Está tu tía (Si / No)").upper()

apetece_helado = apetece_helado_input == "SI"
puedes_permitirtelo = tiene_dinero_input == "SI" or esta_tu_tia_input == "SI"
esta_el_heladero = esta_el_heladero_input == "SI"


if apetece_helado and puedes_permitirtelo and esta_el_heladero:
    print("Pues cómnete un helado")
else:
    print("Pues nada")
