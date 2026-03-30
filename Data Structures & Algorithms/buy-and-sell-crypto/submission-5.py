class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0
        # optional update
        if len(prices)==1:
            return maxProf
        
        curMin = prices[0]
        for val in prices:
            # we have a profitable day
            if val > curMin:
                # attempt to sell
                sell_price = val-curMin
                maxProf = max(maxProf, sell_price)
            else:
                curMin = val


        return maxProf
        