entrada = input("Digite se você quer [E]ntrar ou [S]air: ")
senha = int(input("Digite a sua senha: "))
senha_permitida = (2006)

if entrada == ("E") and senha == senha_permitida:
    print("Você entrou no programa!")
else:
    print("Você saiu do programa!") 


# Se um valor for considerado False, os outros também serão.
# Curto Circuito: Programa para no False.

print(True and False and True)
print(bool("")) # Exibe o valor false (não há um espaço entre o parenteses).
print(True and 0 and True)
# Quando se tem AND, para no valor falsy.

# O Falsy não é um conceito, não é False da forma literal mas é visto como.
# Ex: Lista vazia ---  lista = []