# exercícios básicos de while

#1. faça um programa que imprima de 1 a 10

numero = 1
while numero < 10:
    numero +=1
    print(numero)
    if numero == 10:
        print("Programa acabou! número chegou a 10.")

#2. peça números ao usuário até ele digitar 0. no final, mostre a soma de todos (sem o 0)


input_usuario = None
soma = 0
while input_usuario != 0:
    input_usuario = int(input("Digite um número: "))
    soma = soma + input_usuario
print(f"O programa acabou! o resultado da soma foi {soma}")

#3.diga ao usuário se o programa é Par ou ímpar. programa deve quebrar quando for -1

numero_par_impar = 0

while numero_par_impar != -1:
    numero_par_impar = int(input("Digite um número: "))
    
    if numero_par_impar == -1:
        break
    if numero_par_impar % 2 == 0:
        print("Seu número é par!")
    else:
        print("Seu número é ímpar!")
        
print("Programa acabou! você digitou -1.")

#4. Peça para o usuário digitar a senha até acertar. Senha: 010203
    