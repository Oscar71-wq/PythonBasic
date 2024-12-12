#Escriure un programa que converteixi el números binaris en enters.
def binari(b):
    aux = b[::-1]
    d=0
    for i,e in enumerate(b):
        d+=int(e)*(2**i)
    return d

a = input("introdueix un numero binari: ")
print("el numero {} a decimal és {}".format(a,binari(a)))