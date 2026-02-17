# Crie um código que mostre o resultado da sua divisão
# Crie um except se: Divisão por zero, usuário digitar algo que não seja um número

try:
    numero = float(input("Insira um número que você quer dividir: "))
    n_dividido = float(input("Insira o número que vai dividir o número anterior: "))
    if n_dividido == 0:
        print("O número dividido não pode ser zero.")
    else:
        print(f"O resultado é {numero / n_dividido}")

except:
    print("Digite apenas números.")