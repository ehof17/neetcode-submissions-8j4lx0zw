class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closed = {"}","]",")"}
        open_to_close = {"{":"}", "[":"]", "(":")"}
        close_to_open = {v:k for k,v in open_to_close.items()}
        for thing in s:
            if thing in closed:
                if len(stack)==0:
                    return False
                if close_to_open[thing] != stack[-1]:
                    return False
                stack.pop()
            else:
                stack.append(thing)
        return len(stack) == 0
        