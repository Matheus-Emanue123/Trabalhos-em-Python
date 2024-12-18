import os

def registrar_erro(mensagem):
    with open("gerenciamento_erros.log", "a") as log_file:
        log_file.write(mensagem + "\n")

def criar_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, "w") as arquivo:
            conteudo = input("Digite o conteúdo do arquivo: ")
            arquivo.write(conteudo)
        print(f"Arquivo '{nome_arquivo}' criado com sucesso!")
    except Exception as e:
        registrar_erro(f"Erro ao criar o arquivo '{nome_arquivo}': {e}")
        print("Erro ao criar o arquivo. Verifique o log de erros.")

def abrir_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, "r") as arquivo:
            conteudo = arquivo.read()
            print(f"Conteúdo do arquivo '{nome_arquivo}':\n{conteudo}")
    except FileNotFoundError:
        registrar_erro(f"Arquivo inexistente: '{nome_arquivo}'")
        print("Erro: Arquivo inexistente.")
    except PermissionError:
        registrar_erro(f"Permissões insuficientes para abrir o arquivo '{nome_arquivo}'")
        print("Erro: Permissões insuficientes para abrir o arquivo.")
    except Exception as e:
        registrar_erro(f"Erro inesperado ao abrir o arquivo '{nome_arquivo}': {e}")
        print("Erro inesperado. Verifique o log de erros.")

def editar_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, "a") as arquivo:
            conteudo = input("Digite o conteúdo para adicionar ao arquivo: ")
            arquivo.write("\n" + conteudo)
        print(f"Arquivo '{nome_arquivo}' editado com sucesso!")
    except FileNotFoundError:
        registrar_erro(f"Arquivo inexistente: '{nome_arquivo}'")
        print("Erro: Arquivo inexistente.")
    except PermissionError:
        registrar_erro(f"Permissões insuficientes para editar o arquivo '{nome_arquivo}'")
        print("Erro: Permissões insuficientes para editar o arquivo.")
    except Exception as e:
        registrar_erro(f"Erro inesperado ao editar o arquivo '{nome_arquivo}': {e}")
        print("Erro inesperado. Verifique o log de erros.")

def menu():
    while True:
        print("\nGerenciamento de Arquivos:")
        print("1. Criar arquivo")
        print("2. Abrir arquivo")
        print("3. Editar arquivo")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome do arquivo (com extensão): ")
            criar_arquivo(nome)
        elif opcao == "2":
            nome = input("Digite o nome do arquivo (com extensão): ")
            abrir_arquivo(nome)
        elif opcao == "3":
            nome = input("Digite o nome do arquivo (com extensão): ")
            editar_arquivo(nome)
        elif opcao == "4":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
