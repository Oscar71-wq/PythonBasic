def filtrar_paraules():
    l = []
    while True:
        a = input("Dime una paraula (o un punt per acabar): ")
        if a == ".":
            break
        l.append(a)
    
    x = int(input("Dime un nombre: "))  
    paraules_filtrades = [paraula for paraula in l if len(paraula) > x]
    
    return paraules_filtrades, x

paraules_filtrades, x = filtrar_paraules()

if paraules_filtrades: 
    print("Les paraules amb més de {} caràcters són: {}".format(x, paraules_filtrades)) 
else: 
    print("No hi ha paraules amb més de {} caràcters".format(x))