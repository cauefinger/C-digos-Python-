# crie um script que peça para o usuário digitar o nome de 5 bebidas favoritas dele, armazenando esses valores na lista
# exiba na tela os elementos em ordem alfabética, um por linha utilizando for

bebidas = []

for i in range(5):
    bebida = (input("Digite uma beibida favorita: "))
    bebidas.append(bebida)

bebidas.sort()

print(f"bebidas escolhidas: ")
for bebida in bebidas: 
    print(bebida)

print(f"Saúde!")