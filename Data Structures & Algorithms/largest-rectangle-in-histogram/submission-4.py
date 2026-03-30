class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        for i,h in enumerate(heights):
            start = i
            # cannot continue forward
            while stack and stack[-1][1] > h:
                pi, ph = stack.pop()
                diff = i-pi
                area = ph * diff
                start = pi
                maxArea = max(maxArea, area)

            stack.append((start, h))


        # we still have valid rectangles entirely in stack
        for i, h in stack:
            diff = len(heights) - i
            area = diff * h
            maxArea = max(maxArea, area)

        return maxArea