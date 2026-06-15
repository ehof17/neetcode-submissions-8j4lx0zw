


class Solution:
   
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subs = []
        def helper(i, curlist):
            if i == len(nums):
                subs.append(curlist.copy())
                return
            curlist.append(nums[i])
            helper(i+1, curlist)
            curlist.pop()
            helper(i+1, curlist)
        helper(0,[])
        return subs