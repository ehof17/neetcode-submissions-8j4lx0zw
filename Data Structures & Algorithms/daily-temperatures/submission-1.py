class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # last will be 0
        res = [0] * len(temperatures)
        stack=[]
        for i, val in enumerate(temperatures):
            while stack and val > stack[-1][1]:
                p_i, p_val = stack.pop()
                res[p_i] = i-p_i

            stack.append((i, val))
        return res
       