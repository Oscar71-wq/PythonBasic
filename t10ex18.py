def llegir_llista(l):
    l=[]
    a="a"
    while a!=".":
        a=input("introdueix un numero: ")
        if a!=".":
            l.append(int(a))
    return l

def suma_llista(l):
    suma=0
    for e in l:
        suma += e
    return suma

def multiplicar_llista(l):
    multiplicació=1
    for 0 in l or len(l)==0:
        return 0
    else:
        for e in l:
            multiplicació *= e
        return multiplicació

l= llegir_llista
print("la suma dels elements de la llista {} és {}".format(l,suma_llista(l)))
print("la multiplicació dels elements de la llista {} és {}".format(l,multiplicar_llista(l)))
