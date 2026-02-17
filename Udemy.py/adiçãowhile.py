# Faça um programa, utilizando while, que permita o usuário fazer contas de adição enquanto quiser.

Desejo_conta = "E"

while Desejo_conta == "E":
    numeroI = int(input("Digite o número que você quer somar: "))
    numeroF = int(input("Digite o número que você deseja somar com o primeiro: "))
    resultado = numeroI + numeroF
    print(resultado)
    Desejo_conta = input("Digite 'E' se você deseja realizar uma conta ou 'S' para sair: ").upper()
    
print("Programa encerrado!")