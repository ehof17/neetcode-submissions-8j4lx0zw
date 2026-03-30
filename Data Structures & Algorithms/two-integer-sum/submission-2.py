class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        resmap = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in resmap:
                return [resmap[diff], i]
            resmap[num] = i

        