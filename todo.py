tarefas = ["varrer a casa", "Comprar banana"]

def mostrar_tarefas():
    for indice, tarefa in enumerate(tarefas): 
        print(f"{indice} - {tarefa}")   
    mostrar_linha()

def mostrar_linha():
    print("=" * 30)

while True:
    print("Digite a opção desejada: ")
    mostrar_linha()
    print("Opção 0 = Sair")
    print("Opção 1 = Adicionar ") 
    print( "Opção 2 = Excluir")
    print("Opção 3 = Listar")

    try: 
        opcao = int(input("Opção desejada: "))
    except ValueError:
        print("Por favor, digite apenas números.")
        mostrar_linha()
        continue


    if opcao == 1:
        nova_tarefa = input("Digite uma tarefa: ")
        tarefas.append(nova_tarefa)

        mostrar_tarefas()

    elif opcao == 2:
        mostrar_tarefas()
        indice_a_excluir = int(input("Digite o número da tarefa que você quer excluir: "))
        tarefas.pop(indice_a_excluir)
    elif opcao == 3:
        mostrar_tarefas() 
    elif opcao == 0:
        print("Saindo...")
        mostrar_linha()
        break
    else:
        print("Número inválido! Escolha um número de 0 a 3.")
       