class Solution:
    def rob(self, nums: List[int]) -> int:
        # max
        # rob either max at i or max at i + 1
        if len(nums)<=2:
            return max(nums)
        rob1 = 0 # rob this num
        rob2 = 0
        for num in nums:
            temp = max(num+rob1, rob2)
            
            rob1 = rob2
            rob2 = temp
        return rob2
