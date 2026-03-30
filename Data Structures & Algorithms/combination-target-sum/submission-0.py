

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def helper(i, cur, total):
            # naive case nums[i] divides target
            # then we have nums[i] * x == target
            # check the prevSum
            # if adding the number to the PrevSum makes it larger than the target return

            if total == target:
                res.append(cur.copy())
                return
            if total > target or i >=len(nums):
                return
            
           

            cur.append(nums[i])
            helper(i, cur, total + nums[i])
            cur.pop()
            helper(i+1, cur, total)

        helper(0, [], 0)
        return res

