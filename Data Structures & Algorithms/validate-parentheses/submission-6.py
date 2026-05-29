class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in [')', ']', '}']:
                # close before oen
                if not stack:
                    return False
                if c == ')':
                    if stack[-1]!='(':
                        return False
                    else:
                        stack.pop()
                elif c == ']':
                    if stack[-1]!='[':
                        return False
                    else:
                        stack.pop()
                elif c =='}':
                    if stack[-1]!='{':
                        return False
                    else:
                        stack.pop()
    
            else:
                stack.append(c)
        if stack:
            return False
        else:
            return True
                