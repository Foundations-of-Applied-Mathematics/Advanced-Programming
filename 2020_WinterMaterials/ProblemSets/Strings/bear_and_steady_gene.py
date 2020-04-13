# https://www.hackerrank.com/contests/math-495r-strings/challenges/bear-and-steady-gene/problem

import math
import os
import random
import re
import sys
from collections import deque

# Complete the steadyGene function below.
def steadyGene(gene):
    n = len(gene)
    extras = {C: gene.count(C) for C in ['A', 'G', 'T', 'C'] if gene.count(C) > n//4}
    deficit = {C: gene.count(C) for C in ['A', 'G', 'T', 'C'] if gene.count(C) < n//4}
    total_deficit = sum([v for v in deficit.values()]) - n//4 *len(deficit)

    sub = {'A': 0, 'G': 0, 'T': 0, 'C': 0}
    def valid():
        total_extras = 0
        for k, v in extras.items():
            if sub[k] < v - n//4:
                return False
            total_extras += v
        if total_deficit > total_extras:
            return False
        return True

    s = deque(gene)
    d = deque()
    min_sub = n
    while len(s) > 0:
        while not valid():
            c = s.popleft()
            d.append(c)
            sub[c] += 1
            if len(s) == 0:
                break
        min_sub = min(len(d), min_sub)
        if len(s) == 0 or len(d) == 0:
            break
        c = d.popleft()
        sub[c] += -1
    return min_sub


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    gene = input()

    result = steadyGene(gene)

    fptr.write(str(result) + '\n')

    fptr.close()


