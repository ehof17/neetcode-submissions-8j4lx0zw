import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        neg = [-num for num in nums]
        heapq.heapify(neg)
        while k > 0:
            val = heapq.heappop(neg)
            k-=1
        return -val
