# https://www.hackerrank.com/contests/math-495r-data-structures/challenges/maximize-it/submissions/code/1319418035

in_arr = input().split()
K, M = int(in_arr[0]), int(in_arr[1])
# read in arrays, don't include first number of each line, it describes the number of numbers in the line
arr = [set([(int(i)**2) % M for i in input().split()][1:]) for _ in range(K)]

ans = 0
# possible keeps track of possible answers at every given step
# starts as first set
possible = arr[0]
# iterate through each set and add their values
for i in range(1, K):
    # new contains all possible values after adding the new elements to the previous possible
    new = set([])
    # add all possible combs of elements in possible and arr[i]
    for p in possible:
        for q in arr[i]:
            new.add((p+q) % M)
    possible = new

print(max(possible))
