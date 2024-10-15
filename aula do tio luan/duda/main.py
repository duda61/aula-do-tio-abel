def exibir_menu():
    print("\n" + "="*30)
    print("    Gerenciador de Produtos")
    print("="*30)
    print("1. Adicionar um produto")
    print("2. Exibir o produto mais caro")
    print("3. Listar todos os produtos")
    print("4. Sair")
    print("="*30)

def adicionar_produto(produtos):
    nome = input("Digite o nome do produto: ").strip()
    if not nome:
        print("Nome do produto não pode ser vazio.")
        return
    try:
        preco = float(input(f"Digite o preço de '{nome}': R$ "))
        if preco < 0:
            print("O preço não pode ser negativo.")
            return
    except ValueError:
        print("Preço inválido. Por favor, insira um número.")
        return
    produto = {'nome': nome, 'preco': preco}
    produtos.append(produto)
    print(f"Produto '{nome}' adicionado com sucesso a R$ {preco:.2f}.")

def exibir_produto_mais_caro(produtos):
    if not produtos:
        print("Nenhum produto foi adicionado ainda.")
        return
    produto_caro = max(produtos, key=lambda p: p['preco'])
    print("\n--- Produto Mais Caro ---")
    print(f"Nome: {produto_caro['nome']}")
    print(f"Preço: R$ {produto_caro['preco']:.2f}")

def listar_produtos(produtos):
    if not produtos:
        print("Nenhum produto foi adicionado ainda.")
        return
    print("\n--- Lista de Produtos ---")
    for idx, produto in enumerate(produtos, start=1):
        print(f"{idx}. Nome: {produto['nome']} | Preço: R$ {produto['preco']:.2f}")

def main():
    produtos = []
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()
        if opcao == '1':
            adicionar_produto(produtos)
        elif opcao == '2':
            exibir_produto_mais_caro(produtos)
        elif opcao == '3':
            listar_produtos(produtos)
        elif opcao == '4':
            print("Saindo do programa... Até logo!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
