# Solves all the test cases for https://www.hackerrank.com/challenges/k-factorization/problem
# This problem has very WEAK test cases and can actually be solved by only using a greedy approach. This solution actually calculates all possible solutions (using a greedy method), and then finds and reports the lexicographically smallest, shortest version
# Core idea is to iterate backwards using the largest numbers first, if possible, because these will always end up in the minimum path.

n, k = [int(x) for x in input().strip().split()]
values = sorted([int(x) for x in input().strip().split()])

poss_nums = []
paths = []
for val in values:
    if n % val == 0:
        poss_nums.append(val)
if len(poss_nums) == 0:
    print(-1)
else:
    largest = poss_nums[::-1]
    i = 0
    done = False
    while i < len(largest):
        path = [n]
        sub_larg = largest[i:]
        i += 1
        j = 0
        while j < len(sub_larg):
            larg = sub_larg[j]
            if path[-1] % larg == 0:
                path.append(path[-1] // larg)
            else:
                j += 1
        if path[-1] == 1:
            paths.append((len(path), path[::-1]))
            #print(*path[::-1], sep=" ")
            done = True
            #break
    if done is False:
        print(-1)
    else:
        paths = sorted(paths)
        print(*paths[0][1], sep=" ")