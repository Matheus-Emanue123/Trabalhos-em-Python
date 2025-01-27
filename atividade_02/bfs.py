from collections import deque

def bfs(tabuleiro, m, n):

    movimentos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
   
    fila = deque([(0, 0)])  
    caminho = [[None for _ in range(n)] for _ in range(m)] 
    
    caminho[0][0] = (0, 0)
    
    while fila:
        x, y = fila.popleft()
        
        
        if x == m - 1 and y == n - 1:
            
            caminho_encontrado = []
            while (x, y) != (0, 0):
                caminho_encontrado.append((x, y))
                x, y = caminho[x][y]
            caminho_encontrado.append((0, 0))
            return caminho_encontrado[::-1] 

        for dx, dy in movimentos:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < m and 0 <= ny < n and tabuleiro[nx][ny] == '-' and caminho[nx][ny] is None:
                fila.append((nx, ny))
                caminho[nx][ny] = (x, y)
    
    return None  

# Exemplo de matriz para uso e validação do algoritmo
tabuleiro = [
    ['-', '-', '-', '#', '-', '-'],
    ['#', '#', '-', '#', '-', '#'],
    ['-', '-', '-', '-', '-', '-'],
    ['-', '#', '#', '#', '-', '-'],
    ['-', '-', '-', '#', '-', '-']
]
m, n = len(tabuleiro), len(tabuleiro[0])

caminho = bfs(tabuleiro, m, n)
if caminho:
    print("Caminho encontrado:", caminho)
else:
    print("Não há caminho para a saída.")
