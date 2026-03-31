class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # once its in a fleet then it is in forever
        pairs = [(p, s) for p,s in zip(position, speed)]
        pairs.sort(reverse=True)
        # Get what starts as far back first
        # 
        stack = []
        for p, s in pairs:
            # well have the car thats furthest away first
            # how long to go to target
            # start + (speed * mile/h) = target
            # speed * rate = target - start
            # rate = (target - start) // speed
            rate = (target-p) / s
            # if it is faster than anything before it
            # before it gets bottlenecked
            stack.append(rate)
            if len(stack) >=2 and stack[-1] <= stack[-2]:
                stack.pop()
            
            
        return len(stack)



  
