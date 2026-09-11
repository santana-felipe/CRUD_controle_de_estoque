estoque = [
    {"nome": "Mouse", "quantidade": 10, "preco": 45},
    {"nome": "Teclado", "quantidade": 24, "preco": 80},
    {"nome": "Monitor", "quantidade": 15, "preco": 550}
]


def exibir_produto (produto):
    print(
        f"\nProduto: {produto['nome']}"
        f"\nQuantidade: {produto['quantidade']}"
        f"\nPreço: R${produto['preco']:.2f}"   
    )

def visualizar_estoque():

    print("===========ESTOQUE ATUAL===========")
    for produto in estoque:
        exibir_produto(produto)

    print("===================================")

def buscar_produto(nome):
    for produto in estoque:
        if produto["nome"].lower() == nome.lower():
            return produto

    return None

def cadastrar_produto():
    nome = str(input("\nQual o nome do produto que vai ser cadastrado: ").strip())

    produto = buscar_produto(nome)

    if produto is None:
        try:
            qtd_produto = int(input("\nDigite o estoque do produto: "))

            if qtd_produto <= 0:
                print("\nDigite uma quantidade maior que 0")
                return
            
        except ValueError:
            print("\nDigite uma quantidade válida!")
            return
    else:
        print("\nO produto já existe no estoque!")
        return

    try:
        valor_produto = float(input("Digite o valor do produto: R$").replace(",", "."))

        if valor_produto < 0:
            print("\nDigite um valor maior que zero")
            return
        
    except ValueError:
        print("\nDigite um valor válido!")
        return

    novo_produto = {
        "nome": nome,
        "quantidade": qtd_produto,
        "preco": valor_produto,
    }

    estoque.append(novo_produto)

    print("Produto atualizado!")
    exibir_produto(novo_produto)


def excluir_produto():

    removido = False

    nome = input("\nDigite o nome do produto que vai ser excluido: ").strip()

    produto = buscar_produto(nome)

    if produto is None:
        print("\nProduto não existente. Digite um produto válido!")
        return

    if produto["quantidade"] == 0:
        estoque.remove(produto)
        print("\nProduto removido com sucesso!")
        return

    print("\nO produto não pode ser excluído, quantidade acima de 0")

            
def registrar_entrada():
    nome = input("\nDigite o nome do produto para registrar uma entrada: ").strip()

    produto = buscar_produto(nome)

    if produto is None:
        print("\nProduto não encontrado! Digite um produto válido")
        return

    try:
        qtd_entrada = int(input("Digite a quantidade de entrada: "))

        if qtd_entrada <= 0:
            print("\nA quantidade deve ser maior que zero.")
            return

        produto["quantidade"] += qtd_entrada

        print("Produto atualizado!")
        exibir_produto(nome)

    except ValueError:
        print("\nDigite uma quantidade válida.")

def registrar_saida ():
    nome = input("\nDigite o nome do produto para registar uma saida: ").strip()

    produto = buscar_produto(nome)

    if produto is None:
        print("\nProduto não encontrado! Digite um produto válido!")
        return

    try:
        qtd_saida = int(input("Digite a quantide de saída: "))

        if qtd_saida <= 0:
            print("\nA quantidade deve ser maior que zero")
            return
        
        if qtd_saida > produto["quantidade"]:
            print("\nA quantidade de saída é maior que a quantidade que tem em estoque")
            return

        produto["quantidade"] -= qtd_saida

        print("Produto atualizado!")
        exibir_produto(produto)
        
    except ValueError:

        print("Digite uma quantidade válida")

def iniciar_sistema():
    while True:

        print(
            "\n============================================="
            "\n     Sistema de controle de estoque"
            "\n============================================="
            "\n1 - Visualizar estoque"
            "\n2 - Registrar entrada de produto"
            "\n3 - Registrar saída de produto"
            "\n4 - Cadastrar novo produto"
            "\n5 - Excluir produto"
            "\n6 - Sair do sistema"
        )
        try:
            opcao = int(input("\nDigite a opção que deseja: "))

            if opcao == 1:
                visualizar_estoque()

            elif opcao == 2:
                registrar_entrada()

            elif opcao == 3:
                registrar_saida()

            elif opcao == 4:
                cadastrar_produto()

            elif opcao == 5:
                excluir_produto()
        
            elif opcao == 6:
                break

            else:
                print("\nDigite uma opção válida!")

        except ValueError:
            print("\nDigite uma opção válida!")

iniciar_sistema()