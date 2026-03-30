import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj ={}
        res = {}
        for i in range(1, n+1):
            adj[i] = []

        for u,v,t in times:
            adj[u].append((t, v))

        minHeap=[(0, k)]

        while minHeap:
            time, node = heapq.heappop(minHeap)
            print("Processing node ")
            print(f"Popped min heap weight {time} and node {node}")
            if node in res:
                continue
            res[node] = time
            for t2, n2 in adj[node]:
                heapq.heappush(minHeap,(t2+time, n2))

        if len(res) != n:
            print(len(res))
            print(n)
            print(max(res))
            return -1
        return max(res.values())
            
            


            