import random
N = random.randint(1, 100)
T = [random.randint(1, 10) for i in range(N)]
P = 0.8

edges = []
for i in range(N):
    for j in range(i + 1, N):
        if random.random() < P:
            d = random.randint(10, 12)
            edges.append([i, j, d])
M = len(edges)

print(N)
print(*T)
print(M)
for edge in edges:
    print(*edge)




