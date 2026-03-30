class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numSet = {}
        for i, num in enumerate(nums):
            diff = target - num
            if num in numSet:
                return [numSet[num], i]
            numSet[diff] = i
