class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        for i in range(len(nums)):
            # do we have anything at needed
            needed = target - nums[i]
            if needed in numMap:
                return [numMap[needed], i]
            
            numMap[nums[i]] = i
        



        