def esvocal(x):
    return x.lower() in "aeiou"

a = "a"
while(a!="."):
    a = int("escriu la vocal")
    if esvocal(a):
        print("La lletra introduïda {} és vocal".format(a))
    else:
        print("la lletra introduïda {} no és vocal".format(a))