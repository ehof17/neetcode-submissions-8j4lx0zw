class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        # go until you can't extend
        # while its greater, can go forward
        # only popping most recent element
        # only popping from top to bottom
        # stack contains current heughts we are considering
        # will pop when no longer considering
        # stack [(index, height)]
        maxArea = 0
        # 2, 1
        # once we get to 1
        # we no longer consider the 2
        for i, h in enumerate(heights):
            # no longer consider the 2
            start = i
            while stack and stack[-1][1] > h:
                # see the max area we could have gotten
                si, sh = stack.pop()
                width = i-si
                area = width*sh
                maxArea = max(maxArea, area)
                # since we popped, instead of adding index 1, we can add index 9
                start = si

            stack.append((start,h))
        # if we still have items in the stack
        # we can make them to the end of the histogram
        for i, h in stack:
            width = len(heights)-i
            area = h * width
            maxArea=max(maxArea, area)
        return maxArea
            


