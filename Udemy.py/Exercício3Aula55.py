# Faça um programa que pergunte o nome do usuário. 
# Se o nome tiver 4 letras ou menos escreva "seu nome é curto", se tiver entre 5 e 6 letras escreva "seu nome é normal" e se tiver mais de 6 letras escreva "seu nome é grande"

nome = input("Digite o seu nome: ")
tamanho_nome = len(nome)

if tamanho_nome <= 4:
    print("Seu nome é pequeno.")
elif tamanho_nome >= 5 and tamanho_nome <= 6:
     print("Seu nome é normal.")
else: 
     print("seu nome é muito grande.") 

