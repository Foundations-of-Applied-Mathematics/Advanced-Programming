# This solves all test cases for https://www.hackerrank.com/challenges/xoring-ninja/problem
# I consider this problem easiest to solve by looking at base cases and trying to build up from there.
# Recognize that because we are XORing, each bit is independent of the others.
# so the set {7, 5, 2} is like {111, 101, 010}, but if we are XORing the values together, only values
# of the same columns affect each other, otherwise they remain untouched.

T = int(input())
for _ in range(T):
    n = int(input())
    nums = [int(x) for x in input().strip().split()]
    base = 0
    power = len(nums) - 1
    for p in nums:
        base |= p
    print(base*(2**power) % (10**9 + 7))