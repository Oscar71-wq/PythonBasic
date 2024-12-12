#Definir una funció  mostrar_majors_que() que donada una tupla de números enters, imprimeixi tots els superiors a un altre número donat. Per provar que funciona bé, escriure un programa que permeti introduir els valors enters de la tupla  i ens digui tots els que són majors de 18 anys.
def llegir_llista():
    l=[]
    a="a"
    while a!=".":
        a=input("intodueix una paraula: ")
        if a!=".":
            l.append(int(a))
    return l

def mostrar_majors_que(t , num):
    for e in t:
        if e>min and e<max:
            print("{} es major que {} ".format(e, min, max))

x = llegir_llista()
y = tuple(x)
num=int(input("introdueixi el numero a comparar: "))
mostrar_majors_que(y, min, max)
