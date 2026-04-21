


class Solution:
   
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subs = []
        # either add the number or dont
        def helper(i, currList):
            if i >= len(nums):
                
                subs.append(currList.copy())
                return
            # skip it
            helper(i+1, currList.copy())
            # add it
            currList.append(nums[i])
            helper(i+1, currList.copy())
        helper(0, [])
        return subs