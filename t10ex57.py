def elements_parells(llista):
    
    parells = [paraula for index, paraula in enumerate(llista) if index % 2 == 0]
    return parells

llista_de_paraules = ["pera", "poma", "plàtan", "raïm", "cirera", "préssec", "mandarina"]
paraules_parells = elements_parells(llista_de_paraules)
print(f"Les paraules en posicions parells són: {paraules_parells}")
