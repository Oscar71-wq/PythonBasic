def gran_de_tres(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

exemples = [(3, 5, 2), (10, 8, 12), (7, 7, 7), (4, 9, 9)]
for a, b, c in exemples:
    major = gran_de_tres(a, b, c)
    print(f"Entre {a}, {b} i {c}, el major és {major}.")

        
