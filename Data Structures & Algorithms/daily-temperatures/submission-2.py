class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # last will be 0
        res = [0] * len(temperatures)
        stack=[]
        for i, val in enumerate(temperatures):
            # compare to the value at the top of the stack
            # if the new value is greater, pop it
            while stack and val > stack[-1][1]:
                v_i, v_val = stack.pop()
                diff_i = i - v_i
                res[v_i] = diff_i 
               
            stack.append((i, val))
        return res
       