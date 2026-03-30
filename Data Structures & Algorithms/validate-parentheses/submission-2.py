class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if len(stack) > 0:
                if c == ']' and stack[-1] != '[':
                    print("bre")
                    return False
                elif c == ')' and stack[-1] != '(':
                    print("Taga")
                    return False
                elif c == '}' and stack[-1] != '{':
                    print("this")
                    print(stack[-1])
                    print(stack)
                    return False
                elif c in [']', ')', '}']:
                    stack.pop()
                else:
                    stack.append(c)
            elif c in [']', ')', '}']:
                return False
            else:
                stack.append(c)

        return len(stack) == 0
        