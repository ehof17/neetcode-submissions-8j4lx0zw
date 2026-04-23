import heapq
class Solution:
    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res = []
        for dims in points:
            x,y = dims
            dist = (x**2 + y**2)
            heapq.heappush(heap, (dist, dims))
        while len(res)<k:
            dist, dim = heapq.heappop(heap)
            res.append(dim)
        return res