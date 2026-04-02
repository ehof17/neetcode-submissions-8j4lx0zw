class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        for i, num in enumerate(nums):
            if num in res:
                return [res[num], i]
            val = target-num
            res[val] = i
        
