# https://www.hackerrank.com/contests/math-495r-graphs-2/challenges/dijkstrashortreach
# #!/bin/python3

import math
import os
import random
import re
import sys

# Complete the shortestReach function below.
def shortestReach(n, edges, s):
    max_r = int(1e6)
    # make adjacency matrix
    matrix = [[max_r for r in range(n+1)] for c in range(n+1)]
    for x, y, r in edges:
        matrix[x][y] = min(matrix[x][y], r)
        matrix[y][x] = min(matrix[y][x], r)

    Q = set([i for i in range(1, n+1)])
    d = {i: max_r for i in range(1, n+1)}
    d[s] = 0
    while Q:
        # get min
        min_dist, min_node = max_r+1, -1
        print(d)
        print(Q)
        for k, v in d.items():
            if v < min_dist and k in Q:
                min_dist, min_node = v, k
        Q.remove(min_node)
        for i in range(1, n+1):
            if matrix[min_node][i] != max_r:
                d[i] = min(d[i], d[min_node]+matrix[min_node][i])
    final_distances = []
    for i in range(1, n+1):
        if i != s:
            if d[i] != max_r:
                final_distances.append(d[i])
            else:
                final_distances.append(-1)
    return final_distances

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input())

        result = shortestReach(n, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()


