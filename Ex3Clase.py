"""a = {"nom":"joan","cognom":"ramis","telefon":971360133}
#for e in a:
#   print("{} : {}".format(e,a[e]))
for x,y in a.items():
    print(x,y)
    """
"""a = {"CONTACTE1":{"nom":"joan","cognom":"ramos","telefon":777111223},
    "CONTACTE 2":{"nom":"martí","cognom":"pons","telefon":82727118},
    "CONTACTE 3":{"nom":"maria","cognom":"ramis","telefon":9191024}}
print("Escriure les claus: {}".format(a.keys()))
print("Escriure els valors: {}".format(a.values()))
for x,y in a.items():
    print(x,y)
    """

"""a = int(input("escriu un numero: "))
b = input("escriu un altre numero: ")
c = str(a)+ b
d = a + int(b)
if int(c)>d:
    print("son iguals")
else:
    print("no son iguals")
"""

a = int(input)("Escriu un numero")
b = int(input)("Escriu un numero")
c = int(input)("Escriu un numero")
if a > b:
    if b > c:
        print("{} és major a {} i aqiuest és major que {}".format(a, b, c))
    elif b<c:
        if a>c:
        print("{} és major a {} i aqiuest és major que {}".format(a, b, c))
    elif c>a:
        print("{} és major a {} i aqiuest és major que {}".format(c, a, b)
    else:
        print("{} i {} son iguals i majors que {}".format(a,c,b))
else:

            

