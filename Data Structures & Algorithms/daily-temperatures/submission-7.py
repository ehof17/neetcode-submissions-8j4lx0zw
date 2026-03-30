class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        # push temps to stack
        # pop until we get to a temp hotter
        stack = []
        for i, temp in enumerate(temperatures):
            # if the new val is higher than top of stack
            while stack and stack[-1][1] < temp:
                prev_i, prev_temp = stack.pop()
                diff_i = i - prev_i
                res[prev_i] = diff_i
            stack.append((i, temp))


        


        return res