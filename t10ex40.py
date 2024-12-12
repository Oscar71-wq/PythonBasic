x = int(input("intodueix un numero menor a 100 : "))
y = 0.0
for i in range(1,x,4):
    y +=i**2 
print("la suma dels quadrats de 4 wn 4 de {} és {}".format(x, y))
