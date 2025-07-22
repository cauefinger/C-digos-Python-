# Crie um script que peça para o usuário digitar os nomes de 5 filmes favoritos, armazene-os em uma lista, e exiba os filmes em ordem inversa (do último para o primeiro digitado), um por linha.

filmes = []

for i in range(5):
    filme = (input("Digite o nome de seu filme favorito: "))
    filmes.append(filme)
    filmes.reverse()

print("O nome de seus filmes favoritos são: ")
for filme in filmes:
    print(filme)
   