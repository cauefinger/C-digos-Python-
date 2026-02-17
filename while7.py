#2. peça números ao usuário até ele digitar 0. no final, mostre a soma de todos (sem o 0)

input_usuario = None
soma = 0

while input_usuario != 0:
    input_usuario = int(input("Insira um número: "))

    soma = soma + input_usuario

print(f"A soma é {soma}")