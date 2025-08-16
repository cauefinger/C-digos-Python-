# Juntando 2 tuplas em Python

halogenios = ("F", "Cl", "Br", "I", "At")
gases_nobres = ("Re", "Ne", "Ar", "Xe", "Kr", "Rn")
elementos = halogenios + gases_nobres
print(elementos)
# Junta os elementos e em seguida exibe na tela
print(halogenios[0:4])
# Mostra a lista de halogenios de 0 à 4
print("F" in halogenios)
# Pergunta se o elemento F está presente na tupla de halogenios 
for elemento in elementos:
    print(f'Elemento Químico: {elemento}')
# Cria um laço de repetição for para exibir os elementos na tela