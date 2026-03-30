class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            # check if the current temp is greater than the top of the stack
            while len(stack)>=1 and stack[-1][1]<temp:
                si, st = stack.pop()
                res[si] = i - si
            # if the current temp is greater, we gotta
            stack.append((i, temp))


        return res