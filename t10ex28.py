def majusculas(s):
    num=0
    for e in s:
        if e.isupper():
            num += 1
        return num

a = input("introdueix una paraula amb majusculas i miniusculas: ")
print("el numero de majusculas que te la parula {} es de {}".format(a,majusculas(a)))
