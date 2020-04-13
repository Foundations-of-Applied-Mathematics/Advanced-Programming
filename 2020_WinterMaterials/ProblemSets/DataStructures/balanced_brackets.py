# https://www.hackerrank.com/contests/math-495r-data-structures/challenges/balanced-brackets/copy-from/1319417639
#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque

# Complete the isBalanced function below.
def isBalanced(s):
    # stack for keeping track of current open symbols
    d = deque()
    # dictionary for matching ending chars to start chars
    matches = {')':'(', ']':'[', '}':'{'}
    for c in s:
        # print(d)
        # if c is an ending character
        if c in matches:
            if len(d) == 0:
                return 'NO'
            elif d.pop() != matches[c]:
                return 'NO'
        # c is an opening character
        else:
            d.append(c)
    # if not empty stack at end, some phrases don't terminate
    if len(d) == 0:
        return 'YES'
    else:
        return 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()


