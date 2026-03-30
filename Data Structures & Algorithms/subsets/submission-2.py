


class Solution:
   
    def subsets(self, nums: List[int]) -> List[List[int]]:
        curSet = []
        resSet = []

        def helper(i, curSet):
            if i >= len(nums):
                resSet.append(curSet.copy())
                return
            
            # take it
            curSet.append(nums[i])
            helper(i+1, curSet)
            curSet.pop()

            helper(i+1, curSet)
        helper(0, curSet)
        return resSet