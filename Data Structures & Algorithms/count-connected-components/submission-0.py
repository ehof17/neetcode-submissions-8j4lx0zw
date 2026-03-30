class UnionFind:
    def __init__(self, n):
        self.num_components=n
        self.parents = [i for i in range(n)]
        self.heights = [1] * n

    def find(self, x):
        if x!=self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.heights[root_x] > self.heights[root_y]:
                self.parents[root_y] = root_x
                self.heights[root_x] += self.heights[root_y]
            else:
                self.parents[root_x] = root_y
                self.heights[root_y] += self.heights[root_x]
            self.num_components-=1

            
        return False


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for (x, y) in edges:
            uf.union(x,y)
        return uf.num_components
        