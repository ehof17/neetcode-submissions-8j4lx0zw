class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                val1 = stack.pop()
                val2 = stack.pop()
                val3 = val1 + val2
                stack.append(val3)

            elif token == "-":
                val1 = stack.pop()
                val2 = stack.pop()
                val3 = val2 - val1
                stack.append(val3)

            elif token == "*":
                val1 = stack.pop()
                val2 = stack.pop()
                val3 = val1 * val2
                stack.append(val3)

            elif token == "/":
                val1 = stack.pop()
                val2 = stack.pop()
                val3 = int(float(val2) / val1)
                stack.append(val3)

            else:
                token = int(token)
                stack.append(token)

        return stack.pop()