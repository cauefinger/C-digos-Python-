# informe se este número é par ou ímpar. Caso o usuário não digite um número inteiro, informe que não é um número inteiro.

entrada = input("Digite um número: ")

try:
    entrada_int = int(entrada)
    par_impar = entrada_int % 2 == 0 # criar variável quando necessário para comparação
    if par_impar:
        par_impar_texto = "par"
    else:
        par_impar_texto = "ímpar"
    print(f"O número {entrada_int} é {par_impar_texto}")

except ValueError:
    print("O número digitado não é um número inteiro")