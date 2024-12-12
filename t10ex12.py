def menu():
    op = 0
    print("menu calculadora")
    print("1. sumar")
    print("2. restar")
    print("3. multiplicar")
    print("4. dividir")
    print("5. convertir a octal")
    print("6. convertir a binari")
    print("7. sortir")

    op = int(input("introdueix una opció: "))
    return op

def sumar():
    a = int(input("introdueixi el primer element: "))
    b = int(input("introdueixi el segon element: "))
    c = a + b
    print("El resultat de sumar {} més {} és {}".format(a, b, c))

def restar():
    a = int(input("introdueixi el primer element: "))
    b = int(input("introdueixi el segon element: "))
    c = a - b
    print("El resultat de restar {} menys {} és {}".format(a, b, c))

def multiplicar():
    a = int(input("introdueixi el primer element: "))
    b = int(input("introdueixi el segon element: "))
    c = a * b
    print("El resultat de multiplicar {} per {} és {}".format(a, b, c))

def dividir():
    a = int(input("introdueixi el primer element: "))
    b = int(input("introdueixi el segon element: "))
