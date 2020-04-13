# https://www.hackerrank.com/contests/math-495r-graphs-2/challenges/primsmstsub
import math
import os
import random
import re
import sys
import heapq

# Complete the prims function below.
def prims(n, edges, start):
    max_r = int(1e6)
    # make adjacency matrix
    matrix = [[max_r for r in range(n+1)] for c in range(n+1)]
    for x, y, r in edges:
        matrix[x][y] = min(matrix[x][y], r)
        matrix[y][x] = min(matrix[y][x], r)
    # make visited/unvisited sets
    visited = set([start])
    unvisited = set([i for i in range(1, n+1)])
    unvisited.remove(start)
    total_weight = 0
    potential_edges = []
    # add potential edges
    for j in range(1, n+1):
        if matrix[start][j] != max_r:
            heapq.heappush(potential_edges, (matrix[start][j], start, j))
    # keep adding on min edge
    while len(unvisited) != 0:
        r, v, u = heapq.heappop(potential_edges)
        # keep removing until we reach a valid edge
        while u not in unvisited:
            r, v, u = heapq.heappop(potential_edges)
        unvisited.remove(u)
        visited.add(u)
        for j in range(1, n+1):
            if matrix[u][j] != max_r and j in unvisited:
                heapq.heappush(potential_edges, (matrix[u][j], u, j))
        total_weight += r
    return total_weight


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    edges = []

    for _ in range(m):
        edges.append(list(map(int, input().rstrip().split())))

    start = int(input())

    result = prims(n, edges, start)

    fptr.write(str(result) + '\n')

    fptr.close()
