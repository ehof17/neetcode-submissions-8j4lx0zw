class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0
        # optional update
        if len(prices)==1:
            return maxProf
        
        curMin = prices[0]
        maxProf=0
        for val in prices:
            # if we profit
            if val > curMin:
                sell_price = val - curMin
                maxProf = max(maxProf, sell_price)
            # if we don't profit
            else:
                curMin = val
        return maxProf