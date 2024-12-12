def crear_repetits(n,c):
    return c*n

a=input("introdueix un caracter: ")
b= int(input("dime el nombre de vegades que vols que es repeteixi el caracter anteriaor: "))
print("el caracter {} repetit {} vegades es {}".format(a,b,crear_repetits(b,a)))