import datetime

contatos = []

def inserir_contato():
    nome = input("Digite o nome do contato: ").strip()
    telefone = input("Digite o telefone do contato: ").strip()
    email = input("Digite o email do contato: ").strip()
    aniversario = input("Digite a data de aniversário (DD/MM): ").strip()
    
    contato = {
        'nome': nome,
        'telefone': telefone,
        'email': email,
        'aniversario': aniversario
    }
    contatos.append(contato)
    print(f"Contato {nome} inserido com sucesso!\n")

def remover_contato():
    nome = input("Digite o nome do contato que deseja remover: ").strip()
    global contatos
    contatos = [contato for contato in contatos if contato['nome'].lower() != nome.lower()]
    print(f"Contato {nome} removido com sucesso (se existia)!\n")

def pesquisar_contato():
    nome = input("Digite o nome do contato que deseja pesquisar: ").strip()
    encontrado = False
    for contato in contatos:
        if contato['nome'].lower() == nome.lower():
            print(f"\nNome: {contato['nome']}")
            print(f"Telefone: {contato['telefone']}")
            print(f"Email: {contato['email']}")
            print(f"Aniversário: {contato['aniversario']}\n")
            encontrado = True
            break
    if not encontrado:
        print(f"Contato {nome} não encontrado.\n")

def listar_todos_contatos():
    if not contatos:
        print("Nenhum contato para exibir.\n")
        return
    print("\n--- Lista de Todos os Contatos ---")
    for idx, contato in enumerate(contatos, start=1):
        print(f"{idx}. Nome: {contato['nome']}, Telefone: {contato['telefone']}, Email: {contato['email']}, Aniversário: {contato['aniversario']}")
    print()

def listar_aniversariantes_mes():
    mes_atual = datetime.datetime.now().month
    aniversariantes = []
    for contato in contatos:
        try:
            dia, mes = map(int, contato['aniversario'].split('/'))
            if mes == mes_atual:
                aniversariantes.append(contato)
        except ValueError:
            print(f"Formato de data inválido para o contato {contato['nome']}. Use DD/MM.")
    
    if aniversariantes:
        print(f"\n--- Aniversariantes do Mês ({mes_atual}) ---")
        for contato in aniversariantes:
            print(f"Nome: {contato['nome']}, Aniversário: {contato['aniversario']}")
        print()
    else:
        print("Nenhum aniversariante neste mês.\n")

def exibir_menu():
    print("---- Gerenciador de Contatos ----")
    print("1. Inserir Contato")
    print("2. Remover Contato")
    print("3. Pesquisar Contato")
    print("4. Listar Todos os Contatos")
    print("5. Listar Aniversariantes do Mês")
    print("6. Sair")

def main():
    while True:
        exibir_menu()
        escolha = input("Escolha uma opção: ").strip()
        
        if escolha == '1':
            inserir_contato()
        elif escolha == '2':
            remover_contato()
        elif escolha == '3':
            pesquisar_contato()
        elif escolha == '4':
            listar_todos_contatos()
        elif escolha == '5':
            listar_aniversariantes_mes()
        elif escolha == '6':
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.\n")

if __name__ == "__main__":
    main()