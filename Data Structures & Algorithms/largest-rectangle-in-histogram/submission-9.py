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


        # If the current val is less than top of stack
        # we can no longer go to the right
        # have to pop
        maxArea=0
        for i, height in enumerate(heights):
            ind = i
            while stack and stack[-1][1]>height:
                # after popping this
                # the next one will still need the 
                s_i, s_h = stack.pop()
                currentArea= (i-s_i)*s_h
                maxArea = max(maxArea, currentArea)
                ind=s_i
            stack.append((ind, height))
        # made it to the end
        for i,h in stack:
            maxArea = max(maxArea, h * (len(heights)-i))
        
        return maxArea
        # 321
        # Height 3
        # Height 2
        # Height 1
        
        # But at the 2, we can go backwards
        
        # Need to the boundaries of height
        # 12343
        # 1
        # 12
        # 123
        # 1234
        # 4 is bigger than 3 so pop it
        # On the stack, we should still have
        # (2,3)
        # Current reference is 
        # (4,3)
        # # 



                


            


