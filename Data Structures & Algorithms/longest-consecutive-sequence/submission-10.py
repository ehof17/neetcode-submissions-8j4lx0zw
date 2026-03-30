class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        numSet = set(nums)
        total_longest = 1
        for n in nums:
            if n-1 not in numSet:
                # started
                longest = 1
                while n+longest in numSet:
                    longest+=1
                    total_longest = max(longest, total_longest)

        return total_longest




