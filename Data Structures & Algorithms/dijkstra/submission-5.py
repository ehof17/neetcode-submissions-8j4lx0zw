import heapq
class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = {}
        res = {}
        for i in range(0, n):
            adj[i] = [] 

        for source, destination, weight in edges:
            adj[source].append((destination, weight))

        minHeap = []
        # push the weight
        heapq.heappush(minHeap, (0, src))

        # pop From Da heap
        while minHeap:
            hm = heapq.heappop(minHeap)
            
            cost, node = hm
            if node in res:
                continue
            res[node] = cost
            for adjacent in adj[node]:
                adj_node, adj_cost = adjacent

                heapq.heappush(minHeap, (adj_cost+cost, adj_node))
                    
        
        # go through the neighbors and push
        # cost to reach next value
        # which will be the prev val 
        

        # then rinse and repeat
        for i in range(0, n):
            if i not in res.keys():
                res[i] = -1
        return res

