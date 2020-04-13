import os
import sys

# Complete the merge_sort function below.
def merge_sort(l):
    print(l)
    # base case
    if len(l) == 1:
        return l
    # get middle index
    mid = len(l) // 2
    # stitch two sorted arrays into one sorted array
    def stitch(l1, l2):
        new = []
        done = False
        i, j = 0, 0
        # while elements in both list, add smallest element
        while i < len(l1) and j < len(l2):
            if l1[i] < l2[j]:
                new.append(l1[i])
                i += 1
            else:
                new.append(l2[j])
                j += 1
        # add rest of elements to list
        while i < len(l1):
            new.append(l1[i])
            i += 1
        while j < len(l2):
            new.append(l2[j])
            j += 1
        return new
    return stitch(merge_sort(l[:mid]), merge_sort(l[mid:]))


if __name__ == '__main__':
    t = list(map(int, input().rstrip().split()))
    print(merge_sort(t))
