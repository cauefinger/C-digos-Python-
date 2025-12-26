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
    print("Opção 1 = adicionar ") 
    print( "Opção 2 = excluir")
    print("Opção 3 = listar")
    opcao = int(input("Opção desejada: "))
    mostrar_linha()

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