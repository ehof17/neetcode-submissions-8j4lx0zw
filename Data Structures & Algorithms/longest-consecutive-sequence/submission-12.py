class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)<=1: return len(nums)
        numSet = set(nums)
        longest = 1
        for num in numSet:
            if num-1 not in numSet:
                temp = 1
                while num + temp in numSet:
                    temp+=1
                    longest = max(temp, longest)
        return longest



