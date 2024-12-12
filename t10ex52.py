def crear_llista_fitxer(nom_fitxer):
    llista = []
    try:
        with open(nom_fitxer, 'r', encoding='utf-8') as fitxer:
            for línia in fitxer:
                paraules = línia.split()
                llista.extend(paraules)
    except FileNotFoundError:
        print(f"No s'ha trobat el fitxer {nom_fitxer}.")
    except Exception as e:
        print(f"S'ha produït un error: {e}")
    return llista


nom_fitxer = 'exemple.txt' 
llista_paraules = crear_llista_fitxer(nom_fitxer)
print(f"Les paraules del fitxer són: {llista_paraules}")
