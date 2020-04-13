#!/bin/python3

import os
import sys

# Complete the solve function below.
fact_dict = {0:1}
def factorial(n):
    if n not in fact_dict:
        fact_dict[n] = n * factorial(n-1)
    return fact_dict[n]

def solve(P):
    is_sorted = True
    last = -1
    for p in P:
        if p < last:
            is_sorted = False
        last = p
    if is_sorted:
        return 0

    P.sort()
    n = len(P)
    last = -1
    count = 0
    repeats = {}
    for p in P:
        if p == last:
            count += 1
        elif count > 0:
            repeats[count+1] = repeats.get(count+1, 0) + 1
            count = 0
        last = p
    if count > 0:
        repeats[count+1] = repeats.get(count+1, 0) + 1
    rearrangements = 1
    for k, v in repeats.items():
        rearrangements *= factorial(k) ** v
    # p (probability of a random shuffle being correct) = rearrangements / factorial(k)
    # closed form of solution is 1 / p
    return factorial(n) / rearrangements

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    P_count = int(input())

    P = list(map(int, input().rstrip().split()))

    result = solve(P)

    fptr.write(str(result) + '\n')

    fptr.close()
