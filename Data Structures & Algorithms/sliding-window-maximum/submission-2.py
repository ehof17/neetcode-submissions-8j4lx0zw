class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deq = collections.deque()
        L = R = 0
        output = []
        while R < len(nums):
            # if we encounter a number bigger than the top, pop
            while deq and nums[deq[-1]] < nums[R]:
                deq.pop()

            deq.append(R)

            # if we go out of bounds on the L
            if L > deq[0]:
                deq.popleft()
            
            # window needs to be full length
            if (R+1)>=k:
                output.append(nums[deq[0]])
                L+=1

            R+=1
        return output