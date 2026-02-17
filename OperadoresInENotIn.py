# serve para procurar algo em uma string utilizando a síntese ou digitando o que deseja encontrar

palavra = input("Digite uma palavra: ")
encontrar = input("Digite o que deseja encontrar: ")

if encontrar in palavra:
    print(f"A palavra '{encontrar}' está em {palavra}!")

else:
    print(f"A palavra '{encontrar}' não está em {palavra}...")

# Econtrar utilizando síntese
nome = ("Igor")
print(nome[3])