# Encontrando Caminhos em uma Grade usando Busca em Largura

<div align="center">
    <img src="https://media.giphy.com/media/vVegyymxA90fkY8jkE/giphy.gif" alt="Cat NFT">
</div>

Este programa em Python utiliza o algoritmo de Busca em Largura (BFS) para encontrar o caminho mais curto em uma grade do canto superior esquerdo `(0, 0)` ao canto inferior direito `(m-1, n-1)`. A grade contém células abertas representadas por `'-'` e obstáculos representados por `'#'`.

## Índice

- [Visão Geral](#visão-geral)
- [Como Funciona](#como-funciona)
- [Uso](#uso)
- [Exemplo](#exemplo)

## Visão Geral

O programa busca o caminho mais curto em uma grade semelhante a um labirinto, evitando obstáculos. Ele utiliza BFS para uma busca eficiente de caminhos em grafos ou grades não ponderados.

## Como Funciona

1. **Representação da Grade**: A grade (`tabuleiro`) é uma lista 2D onde cada elemento é `'-'` (caminho aberto) ou `'#'` (obstáculo).

2. **Implementação da BFS**:
    - Inicializa uma fila (`fila`) começando na célula do canto superior esquerdo `(0, 0)`.
    - Explora as células vizinhas em quatro direções: acima, abaixo, esquerda e direita.
    - Mantém o rastreamento do caminho usando a matriz `caminho`.

3. **Reconstrução do Caminho**:
    - Uma vez que o objetivo é alcançado, retrocede usando a matriz `caminho` para reconstruir o percurso.
    - O caminho é retornado como uma lista de coordenadas desde o início até o objetivo.

## Uso

1. **Configuração**:
    - Certifique-se de ter o Python 3 instalado.
    - Salve o código fornecido em um arquivo chamado `main.py`.

2. **Modificar a Grade (Opcional)**:
    - A variável `tabuleiro` define a grade.
    - Personalize-a alterando os elementos `'-'` e `'#'`.

    ```python
    tabuleiro = [
         ['-', '-', '-', '#', '-', '-'],
         ['#', '#', '-', '#', '-', '#'],
         ['-', '-', '-', '-', '-', '-'],
         ['-', '#', '#', '#', '-', '-'],
         ['-', '-', '-', '#', '-', '-']
    ]
    ```

3. **Executar o Programa**:

    ```bash
    python main.py
    ```

4. **Interpretação da Saída**:
    - Se um caminho for encontrado, o programa imprime a sequência de coordenadas.
    - Se nenhum caminho existir, ele imprime uma mensagem indicando a ausência de um caminho.

## Exemplo

Dada a grade padrão, o programa produz:

```
Caminho encontrado: [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 3), (2, 4), (2, 5), (3, 5), (4, 5)]
```

Isso representa o caminho mais curto do início ao objetivo, evitando obstáculos.

