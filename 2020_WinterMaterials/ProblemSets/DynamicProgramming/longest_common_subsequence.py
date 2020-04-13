#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the longestCommonSubsequence function below.
def longestCommonSubsequence(a, b):
    # recursive function
    lcs = {}
    def lcs_rec(i, j):
        # if empty, no common subsequence
        if i < 0 or j < 0:
            return []
        # if already calculated, return
        elif (i, j) in lcs:
            return lcs[(i,j)]
        # if the same, match and add to previous lcs not including either character
        elif a[i] == b[j]:
            last = lcs_rec(i-1, j-1).copy()
            last.append(a[i])
            lcs[(i,j)] = last
            return last
        # if not matched, it is the largest lcs for taking last item on one of the sequences
        else:
            l1 = lcs_rec(i-1, j).copy()
            l2 = lcs_rec(i, j-1).copy()
            last = l1 if len(l1) > len(l2) else l2
            lcs[(i,j)] = last
            return last
    return lcs_rec(len(a) - 1, len(b)-1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = longestCommonSubsequence(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()


