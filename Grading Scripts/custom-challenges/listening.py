import math

cx, cy, N = [int(x) for x in input().split(" ")]
# do a binary search
L = []
for i in range(N):
    x, y, r = [int(x) for x in input().split(" ")]
    L.append((x, y, r))

def dist(a, b, c, d):
    return math.sqrt((a - c)**2 + (b - d)**2)

high = 1000000
low = 0
while True:
    too_big = False
    R = (high + low) / 2
    detection = 0
    for x, y, r in L:
        if dist(cx, cy, x, y) < r + R:
            detection += 1
        if detection == 3:
            too_big = True
            break

    if too_big:
        high = R
    else:
        low = R

    if abs(R - ((high + low) / 2)) < 1e-5:
        break

print(int((high + low) / 2))

            
        
