def helper(i, nums):
    if i == len(nums):
        return [[]]

    resPerms = []
    perms = helper(i+1, nums)
    for p in perms:
        for j in range(len(p)+1):
            cop = p.copy()
            cop.insert(j, nums[i])
            resPerms.append(cop)
    return resPerms

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return helper(0, nums)
        