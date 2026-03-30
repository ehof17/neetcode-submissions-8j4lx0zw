class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deq = collections.deque()
        L = R = 0
        output = []
        while R < len(nums):
            while deq and nums[deq[-1]] < nums[R]:
                deq.pop()

            deq.append(R)

            # if L is out of bounds
            if L > deq[0]:
                deq.popleft()

            # have to consider the full picture
            if R + 1 >= k:
                output.append(nums[deq[0]])
                L+=1
            R+=1
        return output