# https://www.hackerrank.com/contests/math-495r-strings/challenges/hackerrank-in-a-string

import math
import os
import random
import re
import sys

# Complete the hackerrankInString function below.
def hackerrankInString(s):
    i = 0
    for c in 'hackerrank':
        ind = s[i:].find(c)
        if ind == -1:
            return 'NO'
        i += ind +1
    return 'YES'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()
