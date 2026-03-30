class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # go until we find the target
        # once we do, try to shrink it
        result = 0
        minLen = float('inf')
        L = 0
        for R in range(len(nums)):
            while(sum(nums[L:R+1])) >= target:
                minLen = min(minLen, (R-L+1))
                L+=1
                
     
       

        return minLen if minLen != float('inf') else 0

