# Faça um programa, utilizando while, que mostre na tela de 0 até N, em que N é o limite inserido pelo usuário.

N_limite = int(input("Digite o número máximo da contagem: "))
N_inicial = 0

while N_inicial < N_limite:
    N_inicial += 1
    print(N_inicial)