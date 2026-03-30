class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        numSet = set(nums)
        curMax = 1
        for num in nums:
            if num-1 not in numSet:
                diff = 1
                while num+diff in numSet:
                    diff+=1
                curMax = max(curMax, diff)
        return curMax