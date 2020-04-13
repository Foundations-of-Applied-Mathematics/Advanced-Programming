#!/bin/python3

import os
import sys

# Complete the solve function below.
d = {}
def solve(n, m):
    def choose(i, k):
        if (i, k) in d:
            return d[(i,k)]
        if k in (0, i):
            return 1
        d[(i,k)] = (choose(i-1, k-1) + choose(i-1, k)) % (int(1e9) + 7)
        return d[(i,k)]

    return choose(n+m, min(n, m))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        result = solve(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()
