def adicionar_produto(estoque, nome, quantidade, preco):
    if nome in estoque:
        print(f"Produto {nome} já existe no estoque.")
    else:
        estoque[nome] = {'quantidade': quantidade, 'preco': preco}
        print(f"Produto {nome} adicionado com sucesso.")

def atualizar_quantidade(estoque, nome, quantidade):
    if nome in estoque:
        estoque[nome]['quantidade'] += quantidade
        print(f"Quantidade do produto {nome} atualizada com sucesso.")
    else:
        print(f"Produto {nome} não encontrado no estoque.")

def remover_produto(estoque, nome):
    if nome in estoque:
        del estoque[nome]
        print(f"Produto {nome} removido com sucesso.")
    else:
        print(f"Produto {nome} não encontrado no estoque.")

def exibir_relatorio(estoque):
    if not estoque:
        print("Estoque vazio.")
    else:
        total_valor = 0
        print("Relatório de Estoque:")
        for nome, info in estoque.items():
            quantidade = info['quantidade']
            preco = info['preco']
            valor_total_produto = quantidade * preco
            total_valor += valor_total_produto
            print(f"Produto: {nome}, Quantidade: {quantidade}, Preço: {preco:.2f}, Valor Total: {valor_total_produto:.2f}")
        print(f"Valor total do estoque: {total_valor:.2f}")

def main():
    estoque = {}
    while True:
        print("\nMenu:")
        print("1. Adicionar produto")
        print("2. Atualizar quantidade")
        print("3. Remover produto")
        print("4. Exibir relatório")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome do produto: ")
            quantidade = int(input("Quantidade: "))
            preco = float(input("Preço: "))
            adicionar_produto(estoque, nome, quantidade, preco)
        elif opcao == '2':
            nome = input("Nome do produto: ")
            quantidade = int(input("Quantidade a adicionar: "))
            atualizar_quantidade(estoque, nome, quantidade)
        elif opcao == '3':
            nome = input("Nome do produto: ")
            remover_produto(estoque, nome)
        elif opcao == '4':
            exibir_relatorio(estoque)
        elif opcao == '5':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()