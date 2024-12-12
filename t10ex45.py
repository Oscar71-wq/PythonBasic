#Escriure un programa que mostri els dígits parells d’un número donat.
x = input("intro un nombre: ")
i = 0
for e in x:
    if i%2==0:
        print(e)
    i+=1