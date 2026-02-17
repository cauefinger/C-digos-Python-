
entrada = input("Você quer entrar ou sair do sistema?: ")
# Armazena o dado que o usuário digitou

if entrada == ("entrar"): # Compara se a opção "entrar" condiz com o que o usuário digitou
    print("Você entrou no sistema!")
    # Caso a opção digitada for "entrar", exibe a mensagem na tela.

elif entrada == ("sair"): # Compara se a opção "sair" condiz com o que o usuário digitou.
    print("Você saiu do sistema!") 
    # Caso o usuário tenha digitado "sair", exibe essa mensagem na tela.

else: # Opção que o sistema tem se o usuário não digitou nem um, nem outro.
    print("Você não digitou nem 'entrar' nem 'sair'...") 
    # exibe a mensagem na tela se não for nem entrar, nem sair.
