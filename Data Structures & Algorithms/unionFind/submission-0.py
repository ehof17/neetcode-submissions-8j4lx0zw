class UnionFind:
    
    def __init__(self, n: int):
        self.num_components = n
        self.parents = [i for i in range(n)]
        self.heights = [1] * n


    def find(self, x: int) -> int:
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
        

    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


    def union(self, x: int, y: int) -> bool:
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:

            if self.heights[root_x] < self.heights[root_y]:
                self.parents[root_x] = root_y
                self.heights[root_y] += self.heights[root_x]
            else:
                self.parents[root_y] = root_x
                self.heights[root_x] += self.heights[root_y]
            self.num_components-=1
            return True
        return False
        

    def getNumComponents(self) -> int:
        # how many unique parents
        return self.num_components
