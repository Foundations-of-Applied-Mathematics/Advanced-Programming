#!/bin/python3

import math
import os
import random
import re
import sys

def abbreviation(a, b):
    # first index b, second a
    d = {}
    for i, cb in enumerate(b, 1):
        d[(i,0)] = False
    for j, ca in enumerate(a, 1):
        d[(0,j)] = ca.islower() and d.get((0,j-1), True)

    # iterate through substrings of b
    for i, cb in enumerate(b, 1):
        # iterate through substrings of a
        for j, ca in enumerate(a, 1):
            if ca.islower():
                # subproblem possible if can delete lowercase or if can capitalize it and match
                d[(i,j)] = d.get((i, j-1), True) or (ca.upper() == cb and d.get((i-1, j-1), True))
            else:
                # subproblem only possible if can match
                d[(i,j)] = ca == cb and d.get((i-1, j-1), True)
    return 'YES' if d[(len(b), len(a))] else 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        a = input()

        b = input()

        result = abbreviation(a, b)

        fptr.write(result + '\n')

    fptr.close()


