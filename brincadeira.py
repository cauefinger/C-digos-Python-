class Produto:
    def __init__(self, id, nome, quantidade):
        self.id = id
        self.nome = nome
        self.quantidade = quantidade


estoque = []
rodando = True

while rodando:
    print("=================")
    print("Estoque da boca")
    print("Selecione uma opção")
    print("1 - Listar estoque")
    print("2 - Cadastrar produto no estoque")
    print("3 - Realizar venda")
    print("=================")
    opcao = int(input("Insira a opcao desejada: "))
    print("=================")

    if opcao == 1:
        print("Itens em estoque:")
        for produto in estoque:
            print(f"Nome: {produto.nome}, id: {produto.id}, qtd: {produto.quantidade}")
        print("=================")
    if opcao == 2:
        print("Cadastro de produto:")
        nome = input("Insira o nome do produto: ")
        quantidade = input("Insira a quantidade do produto: ")
        produto = Produto(id=len(estoque) + 1, nome=nome, quantidade=quantidade)
        estoque.append(produto)
    if opcao == 3:
        pass
        #TODO: criar uma opção de venda. Deve ter que selecionar um produto pelo id
        # e diminuir 1 do estoque do produto.