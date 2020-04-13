#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pylons function below.
def pylons(k, arr):
    i = 0
    total = 0
    while i < len(arr):
        j = min(len(arr)-1, i+k-1)
        found = False
        while j > i-k:
            if arr[j] == 1:
                i = min(len(arr), j+k)
                total += 1
                found = True
                break
            j += -1
        if not found:
            return -1
    return total



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pylons(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
