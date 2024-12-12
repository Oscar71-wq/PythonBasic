def llegir_llista():
    l=[]
    a=""
    while a!=".":
        a = input("intro un numero dw la llista: ")
        if a!=".":
            l.append(int(a))
    
    return l
def long(l):
    i=0
    for e in l:
        i +=1
        return i

x = llegir_llista