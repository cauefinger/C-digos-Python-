# Crie um programa que gere uma lista de números de 1 a 30
# Crie duas novas listas: uma só com números pares outra só com números ímpares
# Mostre as duas listas quantos números tem em cada

numeros = list(range(1,31))
numero_par = []
numero_impar = []

for numero in numeros:
    if numero % 2 == 0:
        numero_par.append(numero)
    elif numero % 2 != 0:
        numero_impar.append(numero)

print(f"A quantidade de números da lista de pares é {len(numero_par)}")
print(f"A quantidade de números da lista de ímpares é {len(numero_impar)}")