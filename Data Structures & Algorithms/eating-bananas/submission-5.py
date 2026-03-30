class Solution:

    def canComplete(self, piles, k, h):
        # can eat all piles within the time frame
        clock = 0
        for item in piles:
            clock += math.ceil(float(item) / k)

        return clock <= h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minRange = 1
        maxRange = max(piles)
        minVal = maxRange
        # get the mid
        # if we can complete, then try smaller num
        # if we can't complete, try bigger num
        while minRange <= maxRange:
            midVal = (minRange + maxRange) // 2
            
            if self.canComplete(piles, midVal, h):
                minVal = midVal
                maxRange = midVal - 1
            else:
                minRange = midVal + 1
            # check if we can eat them all given the 

        return minVal