def llegir_llista():
    l=[]
    a="a"
    while a!=".":
        a=input("introdueixi un nombre: ")
        if a!=".":
            l.append(int(a))
    return l

def crar_punts():
    s="."
    for e in l:
        for i in range(e):
            print(".")
        print("{} \n".format(s*e))
        s="."

a= llegir_llista()
b= llegir_llista()
crar_punts(a)
crar_punts(b)
crar_punts(a)
