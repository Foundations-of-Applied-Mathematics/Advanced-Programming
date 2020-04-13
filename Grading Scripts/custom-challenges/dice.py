N = [int(x) for x in input().split(" ")]
M = [int(x) for x in input().split(" ")]
N_a = sum(N) / len(N)
M_a = sum(M) / len(M)
if N_a == M_a:
    print("Tie")
elif N_a > M_a:
    print("Amy")
else:
    print("David")
