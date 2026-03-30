class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # check if we already have something -1 or +1 that value
        # then merge the thing
        # for n in nums:
            # if n-1 in minSet
            # merge

        # if num - 1 NOT in array we started sequence
        if not nums:
            return 0
        numSet = set(nums)
        longest = 1
        for num in numSet:
            if (num-1) not in numSet:
                length = 1
                while (num+length) in numSet:
                    length+=1
                    longest = max(length, longest)

        return longest