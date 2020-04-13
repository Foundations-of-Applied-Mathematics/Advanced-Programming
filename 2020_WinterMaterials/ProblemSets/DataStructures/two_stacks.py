# https://www.hackerrank.com/contests/math-495r-data-structures/challenges/game-of-two-stacks/copy-from/1319417792
# !/bin/python3

import os
import sys

#
# Complete the twoStacks function below.
#
def twoStacks(x, a, b):
    # current total added value
    total = 0
    # indices for keeping track of current location in a and b
    i, j = 0, 0
    # push i down a until we've reached total
    while total + a[i] <= x:
        total += a[i]
        i += 1
        if i >= len(a):
            break

    # max number of integers added together, initially max of a
    max_num = i
    # push i up a one at a time
    while i >= 0:
        if j == len(b):
            break
        # push j down b until we reach total
        while total + b[j] <= x:
            total += b[j]
            j += 1
            if j >= len(b):
                break
        max_num = max(max_num, i+j)
        # remove ith element of a
        i += -1
        total += -a[i]
    return max_num

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input())

    for g_itr in range(g):
        nmx = input().split()

        n = int(nmx[0])

        m = int(nmx[1])

        x = int(nmx[2])

        a = list(map(int, input().rstrip().split()))

        b = list(map(int, input().rstrip().split()))

        result = twoStacks(x, a, b)

        fptr.write(str(result) + '\n')

    fptr.close()


