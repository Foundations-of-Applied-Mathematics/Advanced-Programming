# https://www.hackerrank.com/contests/math-495r-data-structures/challenges/merging-communities/copy-from/1319418197

class Node:
    def __init__(self, data):
        self.data = data
        self.parent = self
        self.rank = 0
        self.size = 1

class DSF:
    @staticmethod
    def make_set(data):
        return Node(data)

    @staticmethod
    def find(node):
        if node != node.parent:
            node.parent = DSF.find(node.parent)
        return node.parent

    @staticmethod
    def union(node_a, node_b):
        root_a = DSF.find(node_a)
        root_b = DSF.find(node_b)

        if root_a != root_b:
            if root_a.rank > root_b.rank:
                root_b.parent = root_a
                root_a.size += root_b.size
            else:
                root_a.parent = root_b
                root_b.size += root_a.size
                if root_a.rank == root_b.rank:
                    root_b.rank += 1

N, Q = map(int, input().split())
people = [DSF.make_set(i) for i in range(1, N+1)]
outputs = []

for _ in range(Q):
    inputs = input().split()
    if inputs[0] == 'Q':
        I = int(inputs[1])
        outputs.append(DSF.find(people[I-1]).size)
    elif inputs[0] == 'M':
        I, J = map(int, inputs[1:])
        DSF.union(people[I-1], people[J-1])

for query in outputs:
    print(query)
