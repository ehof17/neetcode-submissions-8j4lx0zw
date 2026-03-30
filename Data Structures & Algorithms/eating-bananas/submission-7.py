import math
class Solution:
    def canComplete(self, piles, k, h):
        # returns if all piles can be processed at K
        res = 0
        for p in piles:


            res+= math.ceil(float(p)/k)
        return res <= h




    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # h = total hours
        # minSpeed = k
        # 
        minVal = 1
        maxVal = max(piles)
        ans = maxVal
        while minVal <=maxVal:
            M = (maxVal+minVal) //2
            if self.canComplete(piles, M, h):
                ans = min(maxVal, M)
                maxVal = M - 1
            else:
                minVal = M + 1
        return ans

