# peça numeros ate o usuario digitar 0

numero = None
numero_digitado = int(input("Digite um número: "))
while numero_digitado != 0:
    while numero_digitado == 0:
        break
    numero_digitado = int(input("Digite mais um número ou 0 para sair: "))
print("O programa acabou! Você digitou 0.")