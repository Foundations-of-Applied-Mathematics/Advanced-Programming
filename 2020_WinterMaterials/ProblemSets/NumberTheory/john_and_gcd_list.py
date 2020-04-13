# https://www.hackerrank.com/contests/math-495r-number-theory/challenges/john-and-gcd-list
#!/bin/python3

import os
import sys
import math

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


def union(d1, d2):
    d = {}
    for k, v in d1.items():
        d[k] = max(v, d2.get(k, 0))
    for k, v in d2.items():
        d[k] = max(v, d1.get(k, 0))
    return d

def multiply(d):
    n = 1
    for k, v in d.items():
        n *= k**v
    return n

# Complete the solve function below.
def solve(a):
    a.append(1)
    b = [a[0]]
    for i in range(len(a)-1):
        d1 = prime_factorization(a[i])
        d2 = prime_factorization(a[i+1])
        b.append(multiply(union(d1,d2)))
    return b

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        a_count = int(input())

        a = list(map(int, input().rstrip().split()))

        result = solve(a)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
