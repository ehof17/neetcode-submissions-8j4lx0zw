class UnionFind:
    def __init__(self, n):
        self.num_connections = n
        self.parents = [i for i in range(n)]
        self.level = [1] * n
    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.level[root_x] > self.level[root_y]:
                self.parents[root_y] = root_x
                self.level[root_x]+= self.level[root_y]

            else:
                self.parents[root_x] = root_y
                self.level[root_y]+= self.level[root_x]


            return True
        return False


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges)+1)
        for edge in edges:
            [x,y] = edge
            if not uf.union(x,y):
                return edge
            
  
        