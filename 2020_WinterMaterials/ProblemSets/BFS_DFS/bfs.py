from collections import deque

# https://www.programiz.com/dsa/graph-bfs
def bfs(graph, root):
    print('bfs')
    visited, queue = set(), deque([root])
    visited.add(root)
    dist = {root: 0}
    while queue:
        # print(queue)
        vertex = queue.popleft()
        print(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                dist[neighbor] = dist[vertex] + 1
                visited.add(neighbor)
                queue.append(neighbor)
    return dist

# # https://www.programiz.com/dsa/graph-dfs
# def dfs(graph, root):
#     print('dfs')
#     visited, queue = set(), deque([root])
#     visited.add(root)
#     dist = {root: 0}
#     while queue:
#         # print(queue)
#         vertex = queue.popleft()
#         print(vertex)
#         for neighbor in list(reversed(graph[vertex])):
#             if neighbor not in visited:
#                 dist[neighbor] = dist[vertex] + 1
#                 visited.add(neighbor)
#                 queue.appendleft(neighbor)
#     return dist

def dfs(graph, root):
    print('dfs')
    visited, queue = set(), deque([root])
    visited.add(root)
    dist = {root: 0}
    while queue:
        # print(queue)
        vertex = queue.popleft()
        print(vertex)
        for neighbor in list(reversed(graph[vertex])):
            if neighbor not in visited:
                dist[neighbor] = dist[vertex] + 1
                visited.add(neighbor)
                queue.appendleft(neighbor)
    return dist


if __name__ == '__main__':
    a, b, c, d, e, f, g, h = 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'
    graph = {a: [b, c], b: [a, d, e], d: [b], e: [b, h], h: [e], c: [a, f, g], f: [c], g: [c]}

    bfs(graph, a)
    dfs(graph, a)
