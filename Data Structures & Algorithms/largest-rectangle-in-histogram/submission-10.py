class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        # go right if the number is greater
        # 
        maxArea = 0
        for i, h in enumerate(heights):
            # keep this variable
            # so we can extend back
            # 1 2 2 1 3 
            # 

            curr_i = i
            while stack and stack[-1][1] > h:
                p_i, p_h = stack.pop()
                curr_i = p_i
                length = i-p_i
                currArea = length*p_h
                maxArea = max(maxArea, currArea)
            stack.append((curr_i, h))
        for i, h in stack:
            calcArea = h * (len(heights)-i)
            maxArea = max(maxArea, calcArea)
        return maxArea

