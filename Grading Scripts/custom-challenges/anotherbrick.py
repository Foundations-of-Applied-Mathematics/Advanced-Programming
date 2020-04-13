import sys

h, w, n = [int(x) for x in input().split(" ")]
bricks = [int(x) for x in input().split(" ")]
brick_ix = 0
for i in range(h):
    rem = w
    while rem > 0:
        if brick_ix == len(bricks):
            print("NO")
            sys.exit(0)
        
        rem -= bricks[brick_ix]
        brick_ix += 1
        if rem < 0:
            print("NO")
            sys.exit(0)
print("YES")
