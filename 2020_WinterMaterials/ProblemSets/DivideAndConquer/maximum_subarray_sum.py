import os
import sys

def maximum_subarray(arr):
    if len(arr) == 1:
        return max(arr[0], 0)
    elif len(arr) == 2:
        return max(arr[0], arr[1], arr[0]+arr[0], 0)
    mid = len(arr) // 2
    max_through_mid = arr[mid-1] + arr[mid]
    left_max, right_max = 0, 0
    left_run, right_run = 0, 0
    i, j = mid-1, mid
    while i >= 0:
        left_run += arr[i]
        left_max = max(left_max, left_run)
        i += -1
    while j < len(arr):
        right_run += arr[j]
        right_max = max(right_max, right_run)
        j += 1
    return max(left_max+right_max, maximum_subarray(arr[:mid]), maximum_subarray(arr[mid:]))

if __name__ == '__main__':
    t = list(map(int, input().rstrip().split()))
    print(maximum_subarray(t))
