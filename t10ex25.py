def llegir_llista():
    l=[]
    a="a"
    while a!=".":
        a=input("introdueixi un nombre: ")
        if a!=".":
            l.append(int(a))
    return l
def gran_llista(l):
    return max(l)

a= llegir_llista()
print("el major de la llista és {}".format(gran_llista(a)))


