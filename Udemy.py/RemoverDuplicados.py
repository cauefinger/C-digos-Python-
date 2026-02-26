# Crie uma nova lista sem valores repetidos mantendo a ordem original.
lista = [1, 2, 2, 3, 4, 3, 5, 1]
nova_lista = [ ]

for numero in lista:
    if numero not in nova_lista:
        nova_lista.append(numero)

print(nova_lista)
    