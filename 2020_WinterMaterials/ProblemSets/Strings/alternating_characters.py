# https://www.hackerrank.com/contests/math-495r-strings/challenges/alternating-characters

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    total = 0
    last_char = ''
    for c in s:
        if c is last_char:
            total += 1
        last_char = c
    return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()


