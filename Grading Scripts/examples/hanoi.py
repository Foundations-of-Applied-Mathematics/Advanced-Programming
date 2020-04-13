import time
memo = {} # maps parameter -> result
def hanoi(n, from_pole, aux_pole, to_pole, moves = 0):
    if n in memo:
        print("I used the memoization table")
        return memo[n]

    if n == 0:
        return moves

    # move n - 1 disks to the aux pole as a position
    moves += hanoi(n - 1, from_pole, to_pole, aux_pole)
    # move the big disk over
    #print("move disk from", from_pole, "to", to_pole)
    moves += 1
    # move the n - 1 disks from the auxiliary pole to the destination pole, using the from_pole
    moves += hanoi(n - 1, aux_pole, from_pole, to_pole)

    # we just did all the computation so might as well save it
    memo[n] = moves
    return moves

#print(hanoi(100, 0, 1, 2))
start_time = time.time()
a = 0
for i in range(8000000):
    a += 1
print("Elapsed: ", time.time() - start_time)

# reduces complexity from 2**n to n
