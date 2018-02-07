# This solves each test case for https://www.hackerrank.com/challenges/components-in-graph/problem
# by implementing a DisjointSet: See https://en.wikipedia.org/wiki/Disjoint-set_data_structure
# Note: this does not implement path compression or flattening, as it is not needed for this problem.

class DisjointSet:
    def __init__(self):
        # self.size_by_parents is a dictionary from key -> # of vertices
        self.size_by_parents = dict()
        #self.parents_by_node is a dictionary from node -> parent
        self.parents_by_node = dict()
        
    def addBtoA(self,a,b):
        """Given two parent nodes, possibly parents of the singleton set,
        Adds the b set, to the 'a' set.
        If we aren't already tracking 'a', begin to do so.
        
        Parameters:
        a (int) - The integer indicating which vertex a is
        b (int) - The integer indicating which vertex b is."""
        if b in self.size_by_parents:
            added_size = self.size_by_parents.pop(b)
        else:
            # if b wasn't a parent, we must be adding a single vertex to the set
            added_size = 1
            
        if a not in self.size_by_parents:
            self.size_by_parents[a] = 1
            self.parents_by_node[a] = a
            
        self.size_by_parents[a] += added_size
        self.parents_by_node[b] = a
    
    def union(self,a,b):
        """Looks up the parents of a and b, if they belong to separate sets we merge set b into a."""
        a_parent = self.findParent(a)
        b_parent = self.findParent(b)
        
        # They belong to different sets, add b to a
        if a_parent != b_parent:
            self.addBtoA(a_parent, b_parent)
        
    def findParent(self,a):
        """Returns the absolute parent of 'a', if 'a' has no parent, then it will return 'a'
        
        Parameters:
        a (int) - A vertex in our graph
        
        Returns:
        parent_a (int)"""
        # if previous ever equals current, we found a node that points to itself
        prev = None
        current = a
        while current in self.parents_by_node:
            current,prev = self.parents_by_node[current], current
            if prev == current:
                return current
        return current
    
dj_set = DisjointSet()
N = int(input())
for _ in range(N):
    a,b = [int(x) for x in input().split()]
    dj_set.union(a,b)
vertices = sorted(dj_set.size_by_parents.values())
print(vertices[0], vertices[-1])