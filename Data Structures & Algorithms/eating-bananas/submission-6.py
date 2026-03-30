class Solution:
    def can_eat(self, piles, h, k):
        res = 0
        for p in piles:
            res+= math.ceil(float(p) / k)
        return res <= h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxVal = max(piles)
        minVal = 1
        ans = maxVal
        while minVal <= maxVal:
            M = (maxVal + minVal) // 2
            if self.can_eat(piles, h, M):
                ans = min(maxVal, M)
                maxVal = M - 1
            else:
                minVal = M + 1
        return ans
        