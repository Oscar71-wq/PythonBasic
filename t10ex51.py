def elimina_duplicats(llista):
    nova_llista = []
    for element in llista:
        if element not in nova_llista:
            nova_llista.append(element)
    return nova_llista


llista_de_prova = [1, 2, 2, 3, 4, 4, 5, 1, 6]
llista_sense_duplicats = elimina_duplicats(llista_de_prova)
print(f"Llista original: {llista_de_prova}")
print(f"Llista sense duplicats: {llista_sense_duplicats}")
