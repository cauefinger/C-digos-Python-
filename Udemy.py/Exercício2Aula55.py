# Faça um programa que pergunte ao usuário e, baseando-se no horário descrito, exiba a saudação apropriada.
# (Bom dia, boa tarde, boa noite)


entrada = (input("Que horas são: "))
horario = int(entrada)
try:
    if horario >= 0 and horario <= 11:
        print("Bom dia!")
    elif horario >= 12 and horario <= 17:
        print("Boa tarde!")
    elif horario >= 18 and horario <=23:
        print("Boa noite!")  
    else:
        print("Não conheço esse horário")
except ValueError:
    print("Você não digitou um número inteiro")