class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L = 0
        R = len(heights) -1
        maxArea = 0
        while L < R:
            minHeight = min(heights[L], heights[R])
            length = R - L
            if minHeight == heights[L]:
                curArea = length * heights[L]
                maxArea = max(maxArea, curArea)
                L+=1
            else:
                curArea = length * heights[R]
                maxArea = max(maxArea, curArea)
                R-=1
        return maxArea


        