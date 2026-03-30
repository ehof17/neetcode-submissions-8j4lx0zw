class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = 0
        maxSum = nums[0]
        for n in nums:
            curSum+=n
            maxSum = max(curSum, maxSum)
            curSum = max(0, curSum)
        
        return maxSum
        

        