import sys
from random import randint

test_n = sys.argv[1]

N = randint(10, 500)
M = randint(1, 4000)
start = randint(0, N - 1)
end = randint(0, N - 1)
edges = []

for i in range(M):
    fr = randint(0, N - 1)
    to = randint(0, N - 1)
    dist = randint(0, 100000)
    
    for j in range(len(edges)):
        if (edges[j][0] == fr and edges[j][1] == to) or (edges[j][1] == fr and edges[j][0] == to):
            break
    else:
        edges.append([fr, to, dist])

M = len(edges)

with open(f"test{test_n}.txt", "w") as f:
    f.write(f"{N} {M}\n")
    for j in range(len(edges)):
        f.write(f"{edges[j][0]} {edges[j][1]} {edges[j][2]}\n")
    f.write(f"{start} {end}")
