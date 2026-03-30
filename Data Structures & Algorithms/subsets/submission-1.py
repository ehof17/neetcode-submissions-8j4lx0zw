def helper(i, nums, curSet, subsets):
    if i >= len(nums):
        subsets.append(curSet.copy())
        return

    curSet.append(nums[i])
    helper(i+1, nums, curSet, subsets)
    curSet.pop()

    helper(i+1, nums, curSet, subsets)





class Solution:
   
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subs = []
        cur = []
        helper(0, nums, cur, subs)
        return subs
