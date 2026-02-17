try:
    numero = float(input("Insira um número que você quer dividir: "))

    if numero < 0:
        raise Exception("O número precisa precisa ser maior que zero")
    
    if numero == 100:
        raise Exception("100 eu não gosto, então não é permitido")

except ValueError:
    print("Digite apenas números.")
except Exception as error:
    print(error)