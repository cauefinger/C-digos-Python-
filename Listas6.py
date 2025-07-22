# Crie um script que peça para o usuário digitar os nomes de 5 filmes favoritos, armazene-os em uma lista, e exiba os filmes em ordem inversa (do último para o primeiro digitado), um por linha.

Filmes = []

for i in range(5):
    Filme = (input(f"Digite seu filme favorito: "))
    Filmes.append(Filme)
    Filmes.reverse()

print(f"filmes escolhidos: ")
for Filme in Filmes:
    print(Filme)