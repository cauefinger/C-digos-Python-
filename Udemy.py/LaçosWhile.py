# Executa uma ação enquanto uma condição for verdadeira
# Loop infinito = quando um código não tem fim

condicao = True
print("Digite 'Sair' para sair.")
while condicao:
    nome = input("Qual é o seu nome? ")
    print (f"seu nome é {nome}. ")
    
    if nome == "Sair":
        break
print("O código acabou! Você saiu do laço.")