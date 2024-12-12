import random

def llegir_llista():
    l=[]
    for _ in range(20):
        l.append(random.randint(1,100))
    print("{}".format(l))
    