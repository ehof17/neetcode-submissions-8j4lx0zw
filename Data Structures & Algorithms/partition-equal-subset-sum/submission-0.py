class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        if totalSum % 2 != 0:
            return False

  
        # try to build a subset with a sum equal to half the total
        targ = totalSum //2

        N, M = len(nums), targ
        memo = [[-1] * (M+1) for _ in range(N+1)]



        def dfs(i, targ):
            if targ == 0:
                return True
            if i >= N or targ < 0:
                return False
            if memo[i][targ] != -1:
                return memo[i][targ]
            
            memo[i][targ] = (dfs(i+1, targ) or dfs(i+1, targ-nums[i]))
            return memo[i][targ]
        return dfs(0, targ)

           