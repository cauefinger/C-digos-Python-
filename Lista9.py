# Faça um programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

numeros_reais = []

for i in range(10):
    numero = float(input("Digite um número real: "))
    print(numero)
    numeros_reais.append(numero)

invertida = numeros_reais[::-1]

print(f"Os números em ordem invertida são: ")
for numero in invertida:
    print(numero)