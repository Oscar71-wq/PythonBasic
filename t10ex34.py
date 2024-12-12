#Definir una funció comptar_vocals() que donada una paraula, compti el número de vegades que apareix cada vocal. Ex: comptar_vocals(“Ratapinyada”) retorni1 HI ha 4 a’s, 0 e’s, 1 i’s, 0 o’s i 0 u’s.
def llegir_llista():
    l =[]
    a = "a"
    while a!=".":
        a=input("Dime una paraula: ")
        if a !=".":
            l.append(a)
    return l

def comptar_vocals(a):
    b = len(a)
    for x in a:
        a = 0
        e= 0
        i = 0
        o = 0
        u = 0
        if x.lower=="a,e,i,o,u":
            a = a+1
            e = e+1
            i = i+1
            o = o+1
            u = u+1
    return x

    print("En la paraula {} hi ha {}".format(a,x))
            
        
    