#defnir una funció paraula_mes_llarga() que donada una llista de paraules, retorni la que té més caràcters. Ex: paraula_mes_llarga([“Hola”, “Ramis”, “IES”, “Paraula”]), ens retorni Paraula.

def paraula_mes_llarga():
    l = []
    a= ""
    while a!=".":
        a = input("introdueix una paraula: ")
        if a!=".":
            l.append(a)


    if not l:
        return None
    
    paraula_mes_llarga = max(l, key = len )
    return paraula_mes_llarga

resultat = paraula_mes_llarga()
if resultat: 
    print("La paraula més llarga és {}".format(resultat))

 