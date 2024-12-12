import random

def llista_20_elements():
    return [random.randint(1, 100) for _ in range(20)]

def elimina_duplicats(llista):
    nova_llista = []
    for element in llista:
        if element not in nova_llista:
            nova_llista.append(element)
    return nova_llista

llista_aleatoria = llista_20_elements()
llista_sense_duplicats = elimina_duplicats(llista_aleatoria)

print(f"Llista generada: {llista_aleatoria}")
print(f"Llista sense duplicats: {llista_sense_duplicats}")

if len(llista_aleatoria) == len(llista_sense_duplicats):
    print("No s'han generat elements duplicats.")
else:
    print("S'han generat elements duplicats.")