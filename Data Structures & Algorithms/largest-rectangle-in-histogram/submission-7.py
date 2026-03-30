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
        for i, h in enumerate(heights):
            # here, if the top of the stack is lower than
            # the height
            # we can no longer go left with our rectangle
            start = i
            while stack and stack[-1][1] > h:
                si, sh = stack.pop()
                diff = i-si
                area = sh*diff
                start = si
                maxArea=max(maxArea, area)

            stack.append((start,h))


        if stack:
            for i, h in stack:
                maxw = len(heights) -i
                area = maxw*h
                maxArea=max(maxArea,area)

        return maxArea
                


            


