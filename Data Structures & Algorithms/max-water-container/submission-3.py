class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # start at end and begining
        # If they cannot connect,
        # Go in the direction that the lower bar was

        # min (heights, L, R)
        L = 0
        R = len(heights) - 1
        res = 0
        while L <= R:
            minHeight = min(heights[L], heights[R])
            curLen = R - L
            res = max(res, minHeight*curLen)
            if heights[L] < heights[R]:
                L+=1
            else:
                R-=1
        return res


        