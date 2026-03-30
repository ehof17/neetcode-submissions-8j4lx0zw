class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # biggest ones first
        memo = {}

        # target = amount - max(coins)
        def dfs(amount):
            if amount == 0:
                return 0
            if amount in memo:
                return memo[amount]
            res = float("inf")
            for coin in coins:
                if amount - coin >= 0:
                    res = min(res, 1 + dfs(amount - coin))

            memo[amount] = res
            return res            

        mincnt = dfs(amount)
        if mincnt >= float("inf"): return -1
        else:
            return mincnt



            