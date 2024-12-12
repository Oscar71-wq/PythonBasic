#Escriure un programa que ens mostri tots els números parells fins arribar a 100. Ex: 2, 4, 6 ...., 98, 100. Prova-la. Fer el mateix amb els números senars.
def numeros_parells():
    parells = []
    for num in range(2, 101, 2):
        parells.append(num)
    print("Números parells fins a 100:", parells)

numeros_parells()

def numeros_senars():
    senars = []
    for num in range(1, 101, 2):
        senars.append(num)
    print("Números senars fins a 100:", senars)

numeros_senars()

