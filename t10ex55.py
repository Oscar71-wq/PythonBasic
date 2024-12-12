def llegir_llista():
    l = []
    a = ""
    while a != ".":
        a = input("Dime un nombre i despre un altre (despres di .): ")
        if a != ".":
            try:
                l.append(int(a))
            except ValueError:
                print(f"'{a}' no és un número vàlid. Introdueix un número.")
    return l

def suma_nombres(l):  
    if len(l) < 2:
        print("Necessites introduir almenys dos números per determinar l'interval.")
        return

    start = l[0]
    end = l[1]
    if start > end:
        start, end = end, start

    suma = sum(range(start, end + 1))
    print(f"La suma de tots els números entre {start} i {end}, ambdós inclosos, és: {suma}")

llista_numeros = llegir_llista()


suma_nombres(llista_numeros)
