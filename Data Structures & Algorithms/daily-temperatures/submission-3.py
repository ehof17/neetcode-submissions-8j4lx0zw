class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i, val in enumerate(temperatures):
            # While the value is greater than the top of the stack
            while stack and stack[-1][1] < val:
                v_i, v_val = stack.pop()
                diff = i - v_i
                res[v_i] = diff
            stack.append((i, val))

        return res