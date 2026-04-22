import heapq
class Solution:
 

    def lastStoneWeight(self, stones: List[int]) -> int:
        neg = [-stone for stone in stones]
        heapq.heapify(neg)
        while len(neg) >=2:
            heaviest = heapq.heappop(neg)
            second = heapq.heappop(neg)
            if heaviest == second:
                continue
            new_weight = heaviest - second
            heapq.heappush(neg, new_weight)
        if len(neg) == 1:
            return -neg[0]
        return 0