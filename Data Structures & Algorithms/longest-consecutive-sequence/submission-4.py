class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0

        numSet = set(nums)
        longest = 1
        for num in numSet:
            if num-1 not in numSet: # started sequence
                curLong = 1
                while (num+curLong in numSet):
                    curLong+=1
                longest = max(longest, curLong)
        return longest