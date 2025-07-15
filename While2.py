# LAÇOS DE REPETIÇÃO TIPO WHILE

nome = None

while True:
    print("Digite seu nome ou X para parar: ")
    nome = input()
    if nome == "X" or nome == "x":
        break
    print(f"Bem vindo, {nome}!")
print("até logo!")