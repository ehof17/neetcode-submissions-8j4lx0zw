class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # start at end and begining
        # If they cannot connect,
        # Go in the direction that the lower bar was

        # min (heights, L, R)
        L, R = 0, len(heights)-1
        maxArea = 0

        while L <= R:
            if heights[L] <= heights[R]:
                area = heights[L] * (R-L)
                maxArea = max(maxArea, area)
                L+=1

            elif heights[L] > heights[R]:
                area = heights[R] * (R-L)
                maxArea = max(maxArea, area)
                R-=1
        return maxArea


        