class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        for i, val in enumerate(nums):
            looking = target - val
            if looking in res:
                return [res[looking], i]
            res[val] = i

        

        