def es_palindrom(cadena):
    cadena = cadena.replace(" ", "").lower()
    return cadena == cadena[::-1]

exemples = ["radar", "ara", "civic", "rallar", "tapat", "simis", "refer", "no és un palíndrom"]
for paraula in exemples:
    resultat = es_palindrom(paraula)
    print(f"'{paraula}' és un palíndrom: {resultat}")
