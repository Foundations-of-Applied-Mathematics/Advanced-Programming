from heapq import heappop, heappush

N, n_edges = [int(x) for x in input().split(" ")]
M = [[-1 if i != j else 0 for i in range(N)] for j in range(N)]

for i in range(n_edges):
    fr, to, dist = [int(x) for x in input().split(" ")]
    M[fr][to] = dist
    M[to][fr] = dist

start, end = [int(x) for x in input().split(" ")]
oo = float("inf")

def dijkstra(start_node, end_node):
  D = [oo for i in range(N)]
  D[start_node] = 0

  q = [(0, start_node)]
  while q:
    d, node = heappop(q)

    if node == end_node:
      return d

    for i in range(len(M[node])):
      if M[node][i] != -1 and M[node][i] != 0 and M[node][i] + d < D[i]:
        D[i] = M[node][i] + d
        heappush(q, (M[node][i] + d, i))
  return -1

print(dijkstra(start, end))



