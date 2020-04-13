# https://www.hackerrank.com/contests/math-495r-number-theory/challenges/identify-smith-numbers

#!/bin/python3

import os
import sys

def digit_sum(n):
    return sum(list(map(int, [d for d in str(n)])))

def prime_factorization(n):
    d = {}
    while n % 2 == 0:
        d[2] = d.get(2, 0) + 1
        n = n // 2
    i = 3
    while i <= n:
        while n % i == 0:
            d[i] = d.get(i, 0) + 1
            n = n // i
        i += 2
    return d

def prime_sum(n):
    d = prime_factorization(n)
    total = 0
    for k, v in d.items():
        total += digit_sum(k) * v
    return total

# Complete the solve function below.
def solve(n):
    return 1 if prime_sum(n) == digit_sum(n) else 0

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = solve(n)

    fptr.write(str(result) + '\n')

    fptr.close()


