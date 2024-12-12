#2 llegir 2 paraules i dir quina es més llarga
"""p = print("Dime una paraula")
p2 = print("Dime una altre paraula")

if len(p) < len(p2):
    print("la paraula més llagra és {}".format(p2))
elif len(p) > len(p2):
    print("la paraula més llarga és {}".format(p))
    """


"""r=list(map(lambda x:x*2,l))
print(r)
"""


"""def pertres(x):
    return x*3
r=list(map(pertres,l))
print (r)
"""

"""l = [2,3,4,5,6]

def elevar5(x):
    return x**5
r=list(map(elevar5, l))
print (r)
"""

#danada una llista que retorni els parells

"""l= [1,2,3,4,5,]
r=[]
for e in l:
    if e%2==0:
        r.append(e)
print(r)
"""
"""def parell(X):
    if x%2==0:
        return True
    return False
r=list(filter(parell,l))
print(r)
"""

"""l = [1,2,3,4,5]
r=list(filter(lambda x:x%2==0,l))
print(r)
"""
n = int(input("introdueix el numero a fer el factorial: "))
i=0
while(i<=n):
    r=r*n
    n=n-1
print(r)