class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            # if bigger than the value at the top of the stack,
            # pop from stack
            # assign res[i] to the current I
            while stack and stack[-1][1] < temp:
                vi, vv = stack.pop()
                diff = i - vi
                res[vi] = diff

            stack.append((i,temp))



        return res