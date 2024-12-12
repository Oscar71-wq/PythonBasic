def llegir_llista():
    l=[]
    a="a"
    while a!=".":
        a=input("introdueixi un nombre: ")
        if a!=".":
             l.append(int(a))
    return l

def superposició(l1, l2):
    for e in l1:
        if e in l2:
            return True
        return False
    
def superposició2(l1, l2):
    ec=[]
    for e in l1:
        if e in l2:
            ec.append(e)
    if len(ec)==0:
        return False, list()
    else:
        return True, ec
    
l=llegir_llista()
s=llegir_llista()
hihaec, ec=superposició2(l,s)
if hihaec:
    print("les dues lleistes {} i {} tenen elements en comú i son{}".format(l, s, ec))
else:
    print("les dues llistes {} i {} no tenen cap element en comú i són {}".format(l, s))
