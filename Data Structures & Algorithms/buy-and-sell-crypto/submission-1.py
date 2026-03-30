class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # prev - curr = pos: 
        maxP = 0
        L=0
        R=1
        while R < len(prices):
            if prices[L] < prices[R]:
                curProf = (prices[R] - prices[L])  
                maxP = max(maxP, curProf)
            else:
                L = R
            R+=1
        return maxP