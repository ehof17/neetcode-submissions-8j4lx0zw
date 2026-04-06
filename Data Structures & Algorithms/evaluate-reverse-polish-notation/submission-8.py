class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        OPERATORS = ['+', '-', '*', '/']
        for tok in tokens:
            if tok in OPERATORS:
                recent_val = int(stack.pop())
                far_val = int(stack.pop())

                match tok:
                    case '+':
                        new_val = recent_val + far_val
                    case '-':
                        new_val = far_val - recent_val
                    case '*':
                        new_val = recent_val*far_val
                    case '/':
                        new_val = far_val / recent_val
                stack.append(new_val)
                
            else:
                stack.append(tok)
        return int(stack.pop())
                
