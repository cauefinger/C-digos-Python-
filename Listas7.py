# Peça ao usuário para digitar 6 itens que ele precisa comprar no mercado. Armazene esses itens em uma lista. 
# Mostre a lista em ordem alfabética 
# Mostre quantos itens tem na lista

compras = []

for i in range(6):
    item = (input(f"Digite os itens que você precisa comprar: "))
    compras.append(item)
print(f"Na sua lista contém: ")
for item in compras:
    print(item)

print(f"A lista tem {len(compras)} elementos.")
