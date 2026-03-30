class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # go until we find the target
        # once we do, try to shrink it
        result = 0
        curSum = 0
        begin = 0
        minLen = float('inf')
        print(minLen)
        for R in range(len(nums)):
            curSum += nums[R]
            while curSum >= target:
                minLen=min(R-begin+1, minLen)
                curSum-=nums[begin]
                begin+=1

        return minLen if minLen != float('inf') else 0

