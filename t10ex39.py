def calcular_capital_final():
    while True:
        cinicial = float(input("Introdueix la quantitat a sol·licitar (mínim 50000€, màxim 800000€): "))
        if 50000 <= cinicial <= 800000:
            break
        else:
            print("Quantitat fora del rang permès. Torna-ho a intentar.")

    while True:
        interes = float(input("Introdueix l'interès (mínim 0.5%, màxim 13%): "))
        if 0.5 <= interes <= 13:
            break
        else:
            print("Interès fora del rang permès. Torna-ho a intentar.")

    while True:
        anys = int(input("Introdueix el nombre d'anys (mínim 3 anys, màxim 40 anys): "))
        if 3 <= anys <= 40:
            break
        else:
            print("Nombre d'anys fora del rang permès. Torna-ho a intentar.")

    cfinal = cinicial * (1 + interes / 100) ** anys

    print(f"El capital final després de {anys} anys serà de: {cfinal:.2f}€")

calcular_capital_final()
