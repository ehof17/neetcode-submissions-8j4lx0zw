class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        OPERATORS = ["+", "-", "*", "/"]
        for tok in tokens:
            if tok not in OPERATORS:
                stack.append(int(tok))
            else:
                s1 = stack.pop()
                s2 = stack.pop()
                if tok == "+":
                    val = s1 + s2
                elif tok == "*":
                    val = s1*s2
                elif tok == "-":
                    val = s2 - s1
                elif tok == "/":
                    val = int(s2/float(s1))
                stack.append(val)

        return int(stack.pop())

                
