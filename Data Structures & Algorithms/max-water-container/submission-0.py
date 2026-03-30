class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # start at end and begining
        # If they cannot connect,
        # Go in the direction that the lower bar was
        L=0
        R= len(heights) -1
        maxHeight = 0
        while L < R:
            minHeight = min(heights[L], heights[R])
            area = minHeight *(R-L)
            maxHeight = max(area, maxHeight)
            if heights[L] < heights[R]:
                L+=1
            else:
                R-=1
        return maxHeight
        