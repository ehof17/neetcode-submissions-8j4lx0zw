class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # cost 

        cache = {}
        def dfs(i):

            if i >= len(cost):
                return 0

            if i in cache:
                return cache[i]

            val = min(
                dfs(i+1),
                dfs(i+2)
            )
            cache[i] = cost[i] + val
            return cache[i]
        
        return min(dfs(0), dfs(1))