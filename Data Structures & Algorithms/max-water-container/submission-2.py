class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # start at end and begining
        # If they cannot connect,
        # Go in the direction that the lower bar was
        L = 0
        R = len(heights) - 1
        res = 0
        while L < R:
            minHeight = min(heights[L], heights[R])
            area = minHeight * (R-L)
            print(f"Area computed {area}")
            res = max(area, res)

            if heights[L] > heights[R]:
                R-=1
            else:
                L+=1
        return res

        