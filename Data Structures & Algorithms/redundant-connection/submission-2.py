
class UnionFind:
    def __init__(self, n):
        self.parents = {}
        self.rank = {}
        for i in range(1, n+1):
            self.parents[i]=i
            self.rank[i]=0
    def find(self, a):
        parent = self.parents[a]
        while parent != self.parents[parent]:
            #self.parents[parent] = self.parents[self.parents[parent]]
            parent = self.parents[parent]
        return parent

    def union(self, a, b):
        # we can make a and set it to child of b
        # If it has a parent
        # how about we find the root node 
        # union the roots together
        pa = self.find(a)
        pb = self.find(b)
        if pa==pb:
            return False
        # smaller rank should be a child of the higher rank

        if self.rank[pa] < self.rank[pb]:
            self.parents[pa] = pb
        elif self.rank[pa] > self.rank[pb]: 
            self.parents[pb] = pa
        else:
            self.parents[pa] = pb
            self.rank[pb]+=1
        return True



class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        uf = UnionFind(n)
        false_cases = []
        for e_a, e_b in edges:
            test = uf.union(e_a, e_b)
            if not test:
                false_cases.append((e_a,e_b))
        worse = false_cases[-1]
        return [worse[0], worse[1]]
        # if not uf.union()