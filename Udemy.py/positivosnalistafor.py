# Contar quantos números positivos existem na lista

lista = [-2, 5, 8, -1, 0, 7, -9]
contador = 0
for i in lista:
    if i >= 0:
        contador += 1
print(f"A quantidade de números positivos na lista é: {contador}.")