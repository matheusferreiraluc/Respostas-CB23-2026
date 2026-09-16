import random
from collections import deque

def generate_maze_iterative(m, n, room=0, wall=1, cheese='.'):
    """
    Gera um labirinto perfeito de m X n células usando DFS iterativo com backtracking.
    """
    maze = [[wall] * (2 * n + 1) for _ in range(2 * m + 1)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    maze[1][1] = room
    stack = [(0, 0)]
    while stack:
        x, y = stack[-1]
        unvisited = []
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and maze[2 * nx + 1][2 * ny + 1] == wall:
                unvisited.append((nx, ny, dx, dy))
        if unvisited:
            # Seleciona um vizinho aleatório
            nx, ny, dx, dy = random.choice(unvisited)  
            # Derruba a parede entre a sala atual e a próxima
            maze[2 * x + 1 + dx][2 * y + 1 + dy] = room
            maze[2 * nx + 1][2 * ny + 1] = room 
            stack.append((nx, ny))
        else:
            stack.pop()

    # Posiciona o queijo em uma sala aleatória garantindo que seja um espaço aberto
    while True:
        i = random.randint(0, 2 * m)
        j = random.randint(0, 2 * n)
        if maze[i][j] == room:
            maze[i][j] = cheese
            break
    return maze


def solve_maze(maze, start=(1, 1)):
    """
    Encontra o caminho do ponto inicial até o queijo usando BFS.
    Retorna a lista de coordenadas representando o caminho.
    """
    rows = len(maze)
    cols = len(maze[0])
    # Busca pela posição do queijo
    cheese_pos = None
    for r in range(rows):
        for c in range(cols):
            if maze[r][c] not in (0, 1, ' ', 'W'):
                cheese_pos = (r, c)
                break
        if cheese_pos:
            break

    queue = deque([(start[0], start[1], [start])])
    visited = set([start])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while queue:
        r, c, path = queue.popleft()
        if (r, c) == cheese_pos:
            return path
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if maze[nr][nc] != 1 and maze[nr][nc] != 'W' and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append((nr, nc, path + [(nr, nc)]))
                    
    return []

def print_maze_and_path(maze, path):
    """
    Imprime o labirinto no terminal, marcando o caminho encontrado com '+'.
    """
    display = [row[:] for row in maze]
    if path:
        for r, c in path[1:-1]:
            display[r][c] = '+'
        display[path[0][0]][path[0][1]] = 'S'
            
    for row in display:
        print(" ".join(str(item) for item in row))


if __name__ == '__main__':
    m, n = 10, 14
    random.seed(10110)
    print("--- Labirinto Gerado ---")
    room, wall, cheese = ' ', 'W', '*'
    maze = generate_maze_iterative(m, n, room, wall, cheese)
    print("\n--- Resolvendo Caminho ---")
    path = solve_maze(maze, start=(1, 1))
    if path:
        print("Caminho encontrado! (S = Início, + = Caminho, * = Queijo)")
        print_maze_and_path(maze, path)
    else:
        print("Nenhum caminho foi encontrado.")