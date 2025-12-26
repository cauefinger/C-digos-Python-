
adicao = 10.5 + 10.5
print(adicao)

potenciacao = 2**10
print(potenciacao)
# numero 2 elevado e ele mesmo 10 vezes

modulo = 25 % 4
print(modulo)
# é o resto da divisão. 
# ex: 6x4 = 24 (módulo é 25) sobra 1


# como descobrir se um número é par 
numero = (8 % 2 == 0)
print(numero)
numero = (7 % 2 == 0)
print(numero)
numero = (924 % 2 == 0)
print(numero)


#                                                   PECULIARIDADES DO PYTHON                                                   #

concatenacao = "juntando" + " " + "palavras" + " " + "exemplo"
print(concatenacao)
# só pode ser feito com o mesmo tipo de dado.

#
"Olá" + " mundo"        # str + str
[1, 2] + [3, 4]         # list + list
(1, 2) + (3, 4)         # tuple + tuple
b"a" + b"b"             # bytes + bytes
#

a_dez_vezes = "A" * 10
print(a_dez_vezes)

cleiton_dez_vezes = "Cleiton " * 10 
print(cleiton_dez_vezes)


# assim como na matemática, o Python segue uma ordem de contar a serem executadas primeiro: 
# 1. (n + n)
# 2. **
# 3. * / // %
# 4. + -
conta_1 = (1 + int(0.5 + 0.5)) ** (5 + 5)
print(conta_1)


# como calcular o IMC

nome = "Cauê Finger"
altura = 1.76
peso = 76
imc = peso / altura ** 2
print(imc)

print(f"O", nome, "tem", altura,"de altura e pesa", peso,"quilos. o seu IMC é de", imc,"." )