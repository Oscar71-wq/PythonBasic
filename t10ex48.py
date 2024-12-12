def hi_ha_duplicats(llista):
    return len(llista) != len(set(llista))

llistes_de_prova = [
    [1, 2, 3, 4, 5],
    [1, 2, 2, 3, 4],
    [10, 20, 30, 40, 50],
    [5, 5, 5, 5, 5],
]

for llista in llistes_de_prova:
    resultat = hi_ha_duplicats(llista)
    print(f"Hi ha duplicats a la llista {llista}? {'Sí' si resultat else 'No'}")
