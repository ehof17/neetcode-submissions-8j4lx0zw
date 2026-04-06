class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minStack:
            if self.minStack[-1] >= val:
                self.minStack.append(val)
            else:
                # what do i do
                pass
        else:
            self.minStack.append(val)



    def pop(self) -> None:
        r_v = self.stack.pop()    
        # 3 3 4
        # 3 3
    
        if self.minStack[-1] == r_v:
            self.minStack.pop()
        
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
       
        
