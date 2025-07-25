# Peça para o usuário digitar 4 nomes de amigos. Depois, pergunte o nome de 1 amigo que ele quer remover da lista.
# Mostre a nova lista após a remoção.

amigos = []

print("A seguir, digite o nome de 4 amigos")
for i in range(4):
    amigo = input("digite o nome de um amigo: ")
    amigos.append(amigo)
   
# mostrar a lista atual de amigos

print("\n sua lista atual de amigos é: ")
print(amigos)

# pedir o nome do amigo que deseja remover

remover = input(f"Digite o nome do amigo que você deseja remover: ")
 
# verifica se o amigo digitado está entre amigos (não não tiver, o código pula pro else)

if remover in amigos:
    amigos.remove(remover)
    print("Amigo removido com sucesso!")

else:
    print("\n Amigo não encontrado na lista. ")

# Mostrar novamente a lista

print("\n lista de amigos atual: ")
print(amigos)
    