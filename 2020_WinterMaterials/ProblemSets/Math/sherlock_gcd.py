#!/bin/python3

import os
import sys

# Complete the solve function below.
def solve(a):
    def gcd(i, j):
        i, j = max(i, j), min(i, j)
        if j == 0:
            return i
        return gcd(j, i%j)
    gcd_sofar = a[0]
    for k in a:
        gcd_sofar = gcd(gcd_sofar, k)
        if gcd_sofar == 1:
            return 'YES'
    return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        a_count = int(input())

        a = list(map(int, input().rstrip().split()))

        result = solve(a)

        fptr.write(result + '\n')

    fptr.close()
