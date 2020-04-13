# https://www.hackerrank.com/contests/math-495r-graphs/challenges/bfsshortreach
#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque

# Complete the bfs function below.
def bfs(n, m, edges, s):
    nodes = [i for i in range(1, n+1)]
    graph = {node: [] for node in nodes}
    for i, j in edges:
        graph[i].append(j)
        graph[j].append(i)

    visited, queue = set(), deque([s])
    visited.add(s)
    d = {node: -1 for node in nodes}
    d[s] = 0
    while queue:
        vertex = queue.popleft()
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                d[neighbor] = d[vertex] + 6
    return [d[i] for i in nodes if i != s]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input())

        result = bfs(n, m, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
