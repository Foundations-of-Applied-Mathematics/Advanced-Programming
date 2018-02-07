# This solves the 2017 ICPC Problem Secret Chamber at Mt. Rushmore.
# The problem was custom-built in HR for a blitz: https://www.hackerrank.com/contests/blitzhard/challenges/secret-chamber-at-mount-rushmore
# See the ACME Advanced Programming class for a reference to ICPC.
# Basically this problem can be solved by simply doing a search across each
# pair of letters to try and convert from c1 to c2. Aka it's just BFS a bunch of times.
# Technically an improvement would be to update our word_dict each time in order to avoid
# searching repetitively, however it is not necessary to solve the problem in the allotted time.

from collections import defaultdict,deque

def bfs(w1,w2,word_dict):
    # Need to check every char in w1 to see if it can become w2
    for c1,c2 in zip(w1,w2):
        if c1 == c2:
            continue
        visited = set()
        marked = set()
        visited.add(c1)
        [marked.add(x) for x in word_dict[c1]]
        marked.add(c1)
        queue = deque(word_dict[c1])
        while len(queue) != 0 and c1 != c2:
            c1 = queue.popleft()
            visited.add(c1)
            for next_ch in word_dict[c1]:
                if next_ch in visited or next_ch in marked:
                    continue
                marked.add(next_ch)
                queue.append(next_ch)
        if c1 == c2:
            continue
        else:
            return 'no'
    return 'yes'
        

chars, words = [int(x) for x in input().strip().split()]
word_dict = defaultdict(lambda: [])
for _ in range(chars):
    start, end = input().strip().split()
    #print(start,end)
    word_dict[start].append(end)

for _ in range(words):
    w1, w2 = input().strip().split()
    if len(w1) != len(w2):
        print("no")
    else:
        print(bfs(w1,w2,word_dict))