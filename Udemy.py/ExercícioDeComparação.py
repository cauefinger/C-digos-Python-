# exibir a variável com o maior valor na tela

valor1 = input("Digite um valor: ")
valor2 = input("Digite mais um valor: ")

if valor1 > valor2:
    print(f"O valor 1, que é {valor1}, é maior que o valor 2, que é {valor2}")
elif valor2 > valor1:
    print(f"O valor 2, que é {valor2}, é maior que o valor 1, que é {valor1}")
else:
    print("Os valores são iguais!")
