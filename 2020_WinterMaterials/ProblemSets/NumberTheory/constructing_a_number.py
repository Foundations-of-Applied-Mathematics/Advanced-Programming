# https://www.hackerrank.com/contests/math-495r-number-theory/challenges/constructing-a-number

import math
import os
import random
import re
import sys

# Complete the canConstruct function below.
def canConstruct(a):
    return 'Yes' if sum(list(map(int, [d for d in ''.join(list(map(str,a)))]))) % 3 == 0 else 'No'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        a = list(map(int, input().rstrip().split()))

        result = canConstruct(a)

        fptr.write(result + '\n')

    fptr.close()
