#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the unboundedKnapsack function below.
def unboundedKnapsack(k, arr):
    d = {0:0}
    for n in range(1, k+1):
        # last value always valid
        d[n] = d[n-1]
        for a in arr:
            last = d.get(n-a, -1)
            if last != -1:
                d[n] = max(d[n], last+a)
    return d[k]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for _ in range(t):

        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        arr = list(map(int, input().rstrip().split()))

        result = unboundedKnapsack(k, arr)

        fptr.write(str(result) + '\n')

    fptr.close()


