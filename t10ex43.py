#Escriure un programa que imprimeixi la taula de multiplicar d’un número donat (mínim 1 màxim 20).
a = int(input(" dime un nombre: "))
for i in range(1,10):
    print("{}x{}={}".format(a, i, a*i))