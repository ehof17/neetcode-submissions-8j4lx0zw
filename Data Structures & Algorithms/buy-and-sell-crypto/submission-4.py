class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #10
        # 1 is less, should buy it
        # 5 is more, shoudlnt buy it
        # should sell since its the highest
        # 6 is more so shouldnt buy it
        # should sell since 5 < 6
        # 7 is more 
        # should sell since 
        L = 0
        R = 1
        if len(prices) == 1:
            return 0
        curMin = prices[L]
        # if smaller than curr min
        maxProf = 0
        while R < len(prices):
            # if the number is less
            should_buy = prices[R]
            # this is the day we should buy
            if should_buy < curMin:
                curMin = should_buy
            # otherwise, attempt to sell
            else:
                maxProf = max(maxProf, prices[R] - curMin)
                L = R
                
            # if the next number is smaller,
            # 10, 1
            # why would we ever buy 10? We would only want to buy 1
            R+=1

        return maxProf
