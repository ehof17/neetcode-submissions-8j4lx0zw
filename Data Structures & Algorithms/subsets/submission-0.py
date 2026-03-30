def helper(i, nums, curSet, subSets):
    if i >= len(nums):
        subSets.append(curSet.copy())
        return

        # decision to take nums i
    curSet.append(nums[i])
    helper(i+1, nums, curSet, subSets)
    curSet.pop()

        # decision to not take nums i
    helper(i+1, nums, curSet, subSets)


class Solution:
   
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subs = []
        cur = []
        helper(0, nums, cur, subs)
        return subs
