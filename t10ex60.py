def es_primer(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def primers_fins_a_100():
    primers = []
    for num in range(1, 101):
        if es_primer(num):
            primers.append(num)
    return primers

numeros_primers = primers_fins_a_100()
quantitat_primers = len(numeros_primers)

print(f"Els números primers entre 1 i 100 són: {numeros_primers}")
print(f"Hi ha {quantitat_primers} números primers entre 1 i 100.")
