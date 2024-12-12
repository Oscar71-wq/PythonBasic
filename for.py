"""def llegir_llista():
    l=[]
    p=""
    while p!=".":
        p=print("introdueix un element de la llista: ")
        if p!=".":
            l.append(int(p))
    return l
#programa
llista = llegir_llista()
r=[]
for i,e in enumerate(llista):
    if i==e:
        r.append(e)
    print("la llista d'elements que coincideix element i posisicioés {}".format(r))
    """

#ex8

def llista_descendent():
    l=[]
    a=True
    u = input("introdueii el primer numero: ")
    l.append(u)
    while a:
        c = input("introdueixi el segon numero: ")
        if c>u:
            a= False
        else:
            l.append(c)
    return l

l= llista_descendent
print("la llista descendent es {}".format(l))
