# função type (serve para identificar qual a função de determinada variável).

import string


media = 0
n1 = n2 = n3 = 0.0
nome, idade = "josué", 25
estado = True

# agora, usarei o a função type para descobrir o tipo de cada varíavel
 
print(type(media))
print(type(n2))
print(type(nome))
print(type(estado))

# função isinstance (se dá uma informação, ao perguntar sobre essa informação ela fala true para sim e false para não)

# a = 10
# b = "sol"
# print(isinstance(a, int))
# print(isinstance(b,str))
# print(isinstance(a,(int,float)))

a = 40
c = 3
r = a * c
print(r)