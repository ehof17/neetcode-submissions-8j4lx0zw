class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        
        maxArea=0
        for i, h in enumerate(heights):
            pushIdx = i
            while stack and stack[-1][1] > h:
                s_i, s_h = stack.pop()
                comp_area = (i-s_i) * s_h
                maxArea = max(maxArea, comp_area)
                pushIdx = s_i
            stack.append((pushIdx, h))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea


