from collections import defaultdict
import heapq
class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
     
        adj = defaultdict(list)
        for i,j,w in edges:
            adj[i].append((w,j))
            adj[j].append((w,i))

        minHeap = []
        for w, n_1 in adj[0]:
            heapq.heappush(minHeap, (w, 0, n_1))
        
        visit = set()
        visit.add(0)
        res = 0
        mst = []
        while minHeap:
            w1, n1, n2 = heapq.heappop(minHeap)
            if n2 in visit:
                continue
            mst.append((w1, n1, n2))
            visit.add(n2)
            res+=w1
            for w,n_4 in adj[n2]:
                if n_4 not in visit:
                    heapq.heappush(minHeap, (w,n2,n_4))

        print(mst)
        print(f"len visit {len(visit)}")
        return res if len(visit) == n else -1

            
        