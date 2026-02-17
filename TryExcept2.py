try:
    valor = float(input("Digite um valor: ")) # se digitar algo que não for um número cai no except por causa do float
    print(valor)
except ValueError:
    print("Isso não é um número")
