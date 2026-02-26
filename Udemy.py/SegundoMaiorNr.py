# Descubra o maior número, descubra o segundo maior número não pode ordenar a lista

numeros = [12, 45, 2, 89, 23, 89, 34, 67]

Maior_Numero = []
Segundo_Maior = []

for numero in numeros:
    if numero > Segundo_Maior:
        numero.append(Maior_Numero)
    elif numero < Maior_Numero:
        numero.append(Segundo_Maior)

print(f"O maior número é o {Maior_Numero} e o segundo maior é o {Segundo_Maior}.")