class Solution:
    def dfs(i, prof, weight, capacity):
        if len(profit) == i:
            return 0
        maxProf = Solution.dfs(i+1, prof, weight, capacity)

        newCap = capacity - weight[i]
        if newCap >= 0:
            p = prof[i] + Solution.dfs(i+1, prof, weight, newCap)
            maxProf = max(maxProf, p)
        return maxProf
        

    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        return Solution.dfs(0,profit, weight, capacity)
