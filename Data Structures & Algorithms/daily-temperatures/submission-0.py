class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # last will be 0
        res = [0] * len(temperatures)
        stack=[]
        for i, val in enumerate(temperatures):
            
            while stack and stack[-1][1] < val:
                hm, hmval = stack.pop()
                res[hm] = (i-hm)
            stack.append((i,val))

        return res