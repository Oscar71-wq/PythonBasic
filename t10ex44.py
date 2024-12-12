#Escriure un programa que sumi els dígits d’un número donat i ens digui si la seva suma és parell o senar.
a = input("introdueix un numero: ")
sum=0
for e in a:
    sum+=int(e)
if sum%2==0:
    print("la suma dels dos digits del numero {} és {} i es parell".format(a, sum))
    print("la suma dels dos digits del numero {} és {} i es senar".format(a, sum))

