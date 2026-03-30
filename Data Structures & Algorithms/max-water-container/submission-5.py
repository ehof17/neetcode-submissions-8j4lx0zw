class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # start at end and begining
        # If they cannot connect,
        # Go in the direction that the lower bar was

        # min (heights, L, R)
        L, R = 0, len(heights)-1
        maxArea = 0
        while L <= R:
            LHeight = heights[L]
            RHeight = heights[R]
            dist = R-L
            area = min(LHeight, RHeight) * dist
            maxArea = max(maxArea, area)
            if LHeight>RHeight:
                R-=1
            else:
                L+=1
        return maxArea


        