# Gerenciador de Contatos 🌌📱

<div align="center">
    <img src="https://media.giphy.com/media/FcQ0aYb0IL0FkHan8z/giphy.gif" alt="Cat NFT">
</div>


Bem-vindo ao **Gerenciador de Contatos**, um aplicativo em Python para gerenciar seus contatos de forma simples e eficiente!

## Índice 📋

- [Funcionalidades](#funcionalidades-)
- [Instalação](#instalação-)
- [Como Usar](#como-usar-)
- [Detalhes do Código](#detalhes-do-código-)
    - [Variáveis Principais](#variáveis-principais-)
    - [Funções Principais](#funções-principais-)
- [Demonstração](#demonstração-)
- [Contribuição](#contribuição-)
- [Licença](#licença-)

## Funcionalidades 🛠

- **Inserir Contato**: Adicione novos contatos com nome, telefone, email e aniversário.
- **Remover Contato**: Remova contatos existentes pelo nome.
- **Pesquisar Contato**: Pesquise informações de um contato específico.
- **Listar Todos os Contatos**: Veja uma lista completa de todos os contatos.
- **Listar Aniversariantes do Mês**: Confira quais contatos fazem aniversário no mês atual.

## Instalação ⚙

1. Certifique-se de ter o Python 3 instalado em seu sistema.
2. Clone este repositório ou faça o download do arquivo `lista_de_contatos.py`.

## Como Usar 🚀

1. Abra o terminal na pasta onde o arquivo está localizado.
2. Execute o script com o comando:

     ```bash
     python lista_de_contatos.py
     ```

3. Siga as instruções apresentadas no menu para interagir com o programa.

## Detalhes do Código 🧩

### Variáveis Principais 📝

- `contatos`: Lista que armazena todos os contatos adicionados. Cada contato é um dicionário com as chaves:
    - `nome`
    - `telefone`
    - `email`
    - `aniversario`

### Funções Principais 🔍

- `inserir_contato()`: Solicita as informações do contato e o adiciona à lista `contatos`.
- `remover_contato()`: Remove um contato da lista com base no nome fornecido.
- `pesquisar_contato()`: Pesquisa e exibe os detalhes de um contato específico.
- `listar_todos_contatos()`: Exibe todos os contatos armazenados.
- `listar_aniversariantes_mes()`: Lista os contatos que fazem aniversário no mês atual.
- `exibir_menu()`: Mostra o menu principal com as opções disponíveis.
- `main()`: Função principal que executa o loop do programa.

## Contribuição 🤝

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## Licença 📄

Este projeto está sob a licença MIT.

---

**Desenvolvido com ❤️ e Python.**
