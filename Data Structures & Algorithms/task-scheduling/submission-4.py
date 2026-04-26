from collections import Counter, deque

import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        q = deque()
        heap = []
        for v in count.values():
            heapq.heappush(heap, -v)
        time = 0
        while heap or q:
            time+=1
            if heap:
                v = heapq.heappop(heap)
                v+=1
                if v < 0:
                    q.append((v, time+n))
            if q and q[0][1]==time:
                qv, qt = q.popleft()
                heapq.heappush(heap, qv)
                
                    


        return time

        
