#!/bin/python3

import math
import os
import random
import re
import sys
import heapq

# Complete the luckBalance function below.
def luckBalance(k, contests):
    max_k = []
    total = 0
    for l, t in contests:
        if t == 0:
            total += l
        else:
            total += -l
            if len(max_k) < k:
                heapq.heappush(max_k, l)
            elif k > 0:
                if l > max_k[0]:
                    heapq.heappop(max_k)
                    heapq.heappush(max_k, l)
    print(max_k)
    for l in max_k:
        total += 2*l
    return total



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
