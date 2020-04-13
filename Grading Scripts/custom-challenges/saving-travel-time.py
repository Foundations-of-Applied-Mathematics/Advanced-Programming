from heapq import heappop, heappush, heapify
from random import randint, seed
from time import time

def solution(n, s, e, paths):
    init_time = time()
    oo = float("inf")
    dists = [oo for i in range(n)]
    D = [[oo if i != j else 0 for i in range(n)] for j in range(n)]

    for path in paths:
        f, t, distance = path
        D[f][t] = distance
        D[t][f] = distance

    init_time = time() - init_time

    calc_time = time()
    q = [(0, s)]
    dists[s] = 0
    while q:
        _, node = heappop(q)

        if node == e:
            calc_time = time() - calc_time
            print("total time: ", init_time + calc_time)
            return dists[e]

        for i in range(len(D[node])):
            if D[node][i] != oo and D[node][i] + dists[node] < dists[i]:
                dists[i] = D[node][i] + dists[node]
                heappush(q, (dists[i], i))
    calc_time = time() - calc_time
    print("total time: ", init_time + calc_time)
    return -1


def test():
    # randomly pick number of nodes, randomly create edges
    # randomly pick a start and end node
    test_cases = []
    seed(4)
    for _ in range(20):

        N = randint(100, 10000)
        N_edges = randint(N, N * 2)
        edges = [[randint(0, N - 1), randint(0, N - 1), randint(1, 1000)] for i in range(N_edges)]
        S = randint(0, N - 1)
        E = randint(0, N - 1)
        test_cases.append([N, S, E, edges])
    return test_cases
    #return [[4, 0, 3, [[0, 1, 1], [0, 2, 4], [1, 2, 2], [1, 3, 7], [2, 3, 1]], 4]]

if __name__ == "__main__":

    n_pos = 0
    n_neg = 0
    for t in test():
        result = solution(t[0], t[1], t[2], t[3])
        n_pos += 1 if result != -1 else 0
        n_neg += 1 if result == -1 else 0

        print("N: ", t[0], "# edges: ", len(t[3]))
        print("Result: ", result)

    print("N positive results: ", n_pos)
    print("N negative results: ", n_neg)
