from heapq import heappop, heappush
import sys

N = int(input())
T = [int(x) for x in input().split(" ")]
M = int(input())
edges = {}
for i in range(M):
    a, b, d = [int(x) for x in input().split(" ")]
    if a - 1 not in edges:
        edges[a - 1] = {}
    if b - 1 not in edges:
        edges[b - 1] = {}
    edges[a - 1][b - 1] = d
    edges[b - 1][a - 1] = d

# dijktra but save paths
oo = float("inf")
shortest_path_dist = -1
D = [oo for i in range(N)]
P = [[] for i in range(N)]
V = set([0])
D[0] = 0
q = [(0, 0)]
while q:
    node, dist = heappop(q)

    if node in edges:
        for neighbor, d in edges[node].items():
            if dist + d < D[neighbor]:
                D[neighbor] = dist + d
                P[neighbor] = [node]
                heappush(q, (neighbor, dist + d))
            elif dist + d == D[neighbor]:
                P[neighbor].append(node)

if D[N - 1] == oo:
    print("impossible")
    sys.exit(0)

print("P: ", P)

def dfs(node, P, T):
    bssf = 0
    if node == 0:
        return T[node]
    for neighbor in P[node]:
        bssf = max(bssf, T[node] + dfs(neighbor, P, T))
    return bssf

print(D[N - 1], dfs(N - 1, P, T))
    
