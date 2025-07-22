# criando algumas funções para lista

L1 = [77, 23, 1, 25, 9, 11]
L2 = [12, 3, 8324, 0, 2]
Valores = L1 + L2
Valores[0] = 9

Valores.append(13)
print(Valores)
# incluir o 13 na lista

Valores.pop()
print(Valores)
# remover o último valor da lista

Valores.pop(2)
print(Valores)
# remover o valor de posição 2 da lista

Valores.insert(4,30)
print(Valores)
# inserir o valor 3o na posição 4

print(20 in Valores)
# confere se o valor 20 está na lista