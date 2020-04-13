# https://www.hackerrank.com/contests/math-495r-graphs/challenges/pacman-bfs
from collections import deque

def adjacency_from_maze(maze):
    h, w = len(maze), len(maze[0])
    d = {}
    for i in range(h):
        for j in range(w):
            if maze[i][j] != '%':
                adj = []
                # up, left, right, down
                for x, y in [(i-1, j), (i, j-1), (i, j+1), (i+1, j)]:
                    if maze[x][y] != '%':
                        adj.append((x, y))
                d[(i, j)] = adj
    return d

def bfs(graph, pacman, food):
    visited, queue = list(), deque([pacman])
    visited.append(pacman)
    prev = {pacman: None}
    while queue:
        vertex = queue.popleft()
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                prev[neighbor] = vertex
                visited.append(neighbor)
                queue.append(neighbor)
                # end when reached food
                if neighbor == food:
                    # print all visited
                    print(len(visited))
                    for i, j in visited:
                        print(f'{i} {j}')
                    return prev

def print_path(prev, food):
    path = []
    current = food
    while current != None:
        path.append(current)
        current = prev[current]
    path = list(reversed(path))
    print(len(path)-1)
    for i, j in path:
        print(f'{i} {j}')


if __name__ == '__main__':
    pacman = tuple(map(int, input().rstrip().split()))
    food = tuple(map(int, input().rstrip().split()))
    size = tuple(map(int, input().rstrip().split()))
    maze = []
    for row in range(size[0]):
        maze.append(input().rstrip())
    # get adjacency matrix
    graph = adjacency_from_maze(maze)

    # get path
    prev = bfs(graph, pacman, food)
    print_path(prev, food)

