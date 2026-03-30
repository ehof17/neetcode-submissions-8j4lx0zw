class MinStack:

    def __init__(self):
       self.stack = []
       self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minStack:
            val_to_push_min = min(self.minStack[-1], val)
        else:
            val_to_push_min = val
        self.minStack.append(val_to_push_min)
       

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        

        
    def top(self) -> int:
        return self.stack[-1]
        
        

    def getMin(self) -> int:
        return self.minStack[-1]
        
