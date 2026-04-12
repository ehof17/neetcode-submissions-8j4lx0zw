import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        res = []
        heap = []
        chunks = len(nums) - k + 1
        L = 0
        R = k
        for i in range(R):
            heapq.heappush(heap, (-nums[i], i))
   
        while R <= len(nums):
            # maxHeap
            while heap[0][1] < L:
                heapq.heappop(heap)
            currMaxVal = -heap[0][0]
            res.append(currMaxVal)
            if R < len(nums):
                heapq.heappush(heap, (-nums[R], R))
            L+=1
            R+=1

        return res