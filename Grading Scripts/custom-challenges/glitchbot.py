import sys
def execute(ins):
    x = 0
    y = 0
    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    d = 0
    for i in range(len(ins)):
        if ins[i] == "Forward":
            x += directions[d][0]
            y += directions[d][1]
        elif ins[i] == "Right":
            d = (d + 1) % len(directions)
        else:
            d -= 1
            if d < 0:
                d = len(directions) - 1
    return (x, y)


X, Y = [int(x) for x in input().split(" ")]
N = int(input())
instructions = []
possible = ["Left", "Forward", "Right"]
for i in range(N):
    instructions.append(input())

for i in range(len(instructions)):
    original = instructions[i]
    for j in range(len(possible)):
        if original != possible[j]:
            instructions[i] = possible[j]
            result = execute(instructions)
            if result[0] == X and result[1] == Y:
                print(i + 1, possible[j])
                sys.exit(0)
    instructions[i] = original
