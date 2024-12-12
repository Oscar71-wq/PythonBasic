def menu():
    op=0
    # while op <1 and op>5:
    print("menu calculadora")
    print("1. sumar")
    print("2. restar")
    print("3. multiplicar")
    print("4. dividir")
    print("sortir")
   

    op = int(input("introdueix una opció: "))
    return op

def sumar():
    a = int(input("introdueixi el primer element"))
    b = int(input("introdueixi el segon element"))
    c = a + b
    print ("el resultat de sumar {} mes {} es {}".format(a, b, c))
def restar():
    a = int(input("introdueixi el primer element"))
    b = int(input("introduexi el segon element"))
    c = a - b
    print ("el resultat de restar {} menys {} es {}".format(a, b, c))
def multiplicar():
    a = int(input("introdueixi el primer element"))
    b = int(input("introdueixi el segon element"))
    c = a * b
    print ("el resultat de multiplicar {} per {} es {}".format(a, b, c))
def dividir():
    a = int(input("introdueixi el primer element"))
    b = int(input("introdueixi el segon element"))
    c = a / b
    print ("el resultat de dividir {} entre {} es {}".format(a, b, c))
a = True
while a:
    op = menu()
    match op:
        case 1:
            sumar()
        case 2:
            restar()
        case 3:
            multiplicar()
        case 4: 
            dividir()
        case 5:
            a = False