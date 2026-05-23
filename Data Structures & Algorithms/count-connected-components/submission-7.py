class unionFind:
    def __init__(self, n):
        self.num_components=n
        self.parents = [i for i in range(n)]
        self.ranks = [1] * n
    def find(self, x):
        if x!=self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, a, b):
        a_p = self.find(a)
        b_p = self.find(b)
        if a_p == b_p:
            return False

        # lower rank should be added to higher rank
        if self.ranks[a_p] > self.ranks[b_p]:
            self.parents[b_p] = a_p
            self.ranks[a_p] +=self.ranks[b_p]
        else: 
            self.parents[a_p] = b_p
            self.ranks[b_p] +=self.ranks[a_p]
        self.num_components-=1


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = unionFind(n)
        for a, b in edges:
            uf.union(a,b)
        return uf.num_components