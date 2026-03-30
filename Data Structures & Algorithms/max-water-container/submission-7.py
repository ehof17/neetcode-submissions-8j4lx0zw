class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L, R = 0, len(heights)-1
        res = 0

        while L <= R:
            if heights[L] < heights[R]:
                minHeight = heights[L]
                area = minHeight * (R-L)
                res = max(area,res)
                L+=1
            
            else:
                minHeight = heights[R]
                area = minHeight * (R-L)
                res = max(area,res)
                R-=1



        return res



        