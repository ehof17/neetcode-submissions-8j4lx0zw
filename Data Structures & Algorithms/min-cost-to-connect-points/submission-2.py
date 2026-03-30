import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) == 0:
            return 0
        adj = {}
        
        for i, (x, y) in enumerate(points):
            adj[i] = []
            for j in range(len(points)):
                if j == i:
                    continue
                dist_x =  abs(points[j][0] - points[i][0])
                dist_y =  abs(points[j][1] - points[i][1])
                dist = dist_x+dist_y
                adj[i].append((dist,j))
       


        minHeap = []
        for w, neighbor in adj[0]:
            heapq.heappush(minHeap, (w, 0, neighbor))
        visit = set()
        visit.add(0)

        
        mst = []
        val = 0
        while minHeap:
            print(len(visit))
            w1, n1, n2 = heapq.heappop(minHeap)
            if n2 not in visit:
                visit.add(n2)
                mst.append((w1,n1,n2))
                val+=w1
                for w2,j in adj[n2]:
                    if j not in visit:
                        heapq.heappush(minHeap, (w2, n2, j))

        return val



      

        