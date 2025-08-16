
halogenios = ("F", "Cl", "Br", "I", "At")
gases_nobres = ("Re", "Ne", "Ar", "Xe", "Kr", "Rn")
elementos = halogenios + gases_nobres

# transformar a tupla de halogenios em uma lista

grupo17 = list(halogenios)
grupo17[0] = "H"
# adiciona um novo elemento para a lista
print(grupo17)