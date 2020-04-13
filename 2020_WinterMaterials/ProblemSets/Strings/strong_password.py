# https://www.hackerrank.com/contests/math-495r-strings/challenges/strong-password/submissions/code/1319660497

import math
import os
import random
import re
import sys

# Complete the minimumNumber function below.
def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"

    def intersects(a, b):
        for c in a:
            if c in b:
                return True
        return False

    total = 0
    if not intersects(numbers, password):
        total += 1
    if not intersects(lower_case, password):
        total += 1
    if not intersects(upper_case, password):
        total += 1
    if not intersects(special_characters, password):
        total += 1

    return max(total, 6-len(password))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
