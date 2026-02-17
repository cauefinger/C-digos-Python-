nome = input("Digite seu nome: ")

print(f"Seu nome invertido é {nome[::-1]}")

if " " in nome:
    print("O seu nome contém espaços.")
else:
    print("O seu nome não contém espaços.")

print(f"O seu nome contém {len(nome)} letras.")

print(f"A primeira letra do seu nome é '{nome[0]}'.")

print(f"A última letra do seu nome é {nome[-1]}.")

if nome == (""):
    print("Desculpe, você deixou campos vazios.")
else:
    print(f"O seu nome é {nome}")


