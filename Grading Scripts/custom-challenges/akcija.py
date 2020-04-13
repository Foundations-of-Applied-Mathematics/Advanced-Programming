import sys

L= [x.strip() for x in sys.stdin.readlines()]
lines = [int(x) for x in L[1:]]
lines = sorted(lines, reverse = True)
price = 0
for i in range(len(lines)):
    if (i + 1) % 3 == 0:
        continue
    price += lines[i]
print(price)
