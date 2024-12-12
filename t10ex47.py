def esta_ordenada(llista):
    if llista == sorted(llista):
        return "La llista està ordenada de forma ascendent."
    elif llista == sorted(llista, reverse=True):
        return "La llista està ordenada de forma descendent."
    else:
        return "La llista no està ordenada."


exemples = [
    [3, 2, 1],    
    [4, 5, 6],   
    [1, 3, 2],    
    [7, 7, 7],    
    [10, 9, 8, 8, 7]  
]

for exemple in exemples:
    resultat = esta_ordenada(exemple)
    print(f"Llista: {exemple} => {resultat}")

