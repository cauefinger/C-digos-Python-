# Crie uma calculadora que aceita os operadores de adição, subtração, multiplicação e divisão

while True:
    sair = input("Digite [s]air para encerrar o programa: ").lower().startswith("s")
    if sair == True:
        break
    numero1 = int(input("Digite o primeiro número: "))
    operador = input("Digite o operador que você deseja (+, -, /, *) ")
    numero2 = int(input("Digite o segundo número: "))
    if operador == "+":
        print(numero1 + numero2)
    elif operador == "-":
        print (numero1 - numero2)
    elif operador == "*":
        print (numero1 * numero2)
    elif operador == "/":
        print (numero1 / numero2)
print("Programa encerrado! Opção 'sair' foi selecionada.")