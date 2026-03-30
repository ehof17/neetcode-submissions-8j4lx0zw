


class Solution:
   
    def subsets(self, nums: List[int]) -> List[List[int]]:
        curSet = []
        resSet = []

        def helper(i, curSet, resSet, nums):
            if i >= len(nums):
                resSet.append(curSet.copy())
                return
            
            helper(i+1, curSet, resSet, nums)

            curSet.append(nums[i])
            helper(i+1, curSet, resSet, nums)
            curSet.pop()

        helper(0, curSet, resSet, nums)
        return resSet