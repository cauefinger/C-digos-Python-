# faça um código que imprima o valor na tela, se o valor for fazio tratar com if e tratar o erro caso o valor não seja um número
valor = input("Digite um número: ")
if valor == "":
    print("Erro! valores vazios não são aceitos.")
else:   
    try:
        print(int(valor))
    except ValueError:
        print("Erro! o que foi digitado não é um número. ")
  