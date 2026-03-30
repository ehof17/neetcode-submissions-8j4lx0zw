class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            # if the temp is greater than what we have in the stack
            while stack and stack[-1][1] < temp:
                si, sv = stack.pop()
                diff = i -si
                res[si] = diff

            stack.append((i, temp))


        return res