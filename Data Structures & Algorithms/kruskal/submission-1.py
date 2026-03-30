import heapq
class UnionFind:
    def __init__(self, n):
        self.num_components = n
        self.parents = [i for i in range(n)]
        self.heights = [1] * n

    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:

            if self.heights[root_x] < self.heights[root_y]:
                self.parents[root_x] = root_y
                self.heights[root_y] += self.heights[root_x]
            else:
                self.parents[root_y] = root_x
                self.heights[root_x] += self.heights[root_y]
            
            return True
        return False



class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        minHeap = []
        for n1, n2, w1 in edges:
            heapq.heappush(minHeap, (w1, n1, n2))
        mst = []
        res = 0
        while len(mst) < n-1:
            try:
                w2, n3, n4 = heapq.heappop(minHeap)
            except IndexError as e:
                return -1
            if not uf.union(n3, n4):
                continue
            mst.append([n3, n4])
            res+= w2
        return res

