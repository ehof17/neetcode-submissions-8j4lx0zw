class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deq = collections.deque()
        res = []
        L = R = 0
        while R < len(nums):
            while deq and nums[deq[-1]] < nums[R]:
                deq.pop()

            deq.append(R)

            if L > deq[0]:
                deq.popleft()

            if R + 1 >= k:
                res.append(nums[deq[0]])
                L+=1

            R+=1
        return res