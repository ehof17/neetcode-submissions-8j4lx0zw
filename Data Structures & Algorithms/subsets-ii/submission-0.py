def helper(i, nums, subs, cur):
    if i >= len(nums):
        subs.append(cur.copy())
        return

    # if multiple we need to include however many iunacatances
    
    # take nums
    cur.append(nums[i])
    helper(i+1, nums, subs, cur)
    cur.pop()

    # dont take nums
    while i + 1 < len(nums) and nums[i] == nums[i+1]:
        i+=1
    helper(i+1, nums, subs, cur)


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subs, cur = [], []
        sorted_nums = sorted(nums)
        helper(0, sorted_nums, subs, cur)
        return subs