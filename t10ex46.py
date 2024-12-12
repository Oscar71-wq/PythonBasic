#Definir una funció eliminarcapicua() que donada una llista, elimini el primer i el darrer element de la llista i ens retorni una nova llista sense aquest dos elements. Prova-la
def eliminarcapicua(llista):
    if len(llista) > 1:
        return llista[1:-1]
    else:
        return []

# Provar la funció amb una llista d'exemple
llista_de_prova = [1, 2, 3, 4, 5]
nova_llista = eliminarcapicua(llista_de_prova)
print(f"Llista original: {llista_de_prova}")
print(f"Llista sense el primer i el darrer element: {nova_llista}")


