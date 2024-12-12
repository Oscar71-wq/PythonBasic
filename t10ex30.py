def calcular_edats(any_actual, persones):
    dades = []
    for nom, any_naixement in persones:
        edat = any_actual - any_naixement
        dades.append((nom, any_naixement, edat))
    return dades

def imprimir_taula(dades):
    print(f"{'Nom':<20}{'Any de Naixement':<20}{'Edat':<10}")
    print("-" * 50)
    for nom, any_naixement, edat in dades:
        print(f"{nom:<20}{any_naixement:<20}{edat:<10}")

# Any actual
any_actual = 2024

# Dades de les persones
persones = [
    ("Maria", 1990),
    ("Joan", 1985),
    ("Anna", 2000),
    ("Pere", 1975)
]

