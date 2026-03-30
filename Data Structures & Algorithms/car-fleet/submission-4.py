class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # once its in a fleet then it is in forever
        pairs = [(p, s) for p,s in zip(position, speed)]
        pairs.sort(reverse=True)
        print(pairs)
        stack = []
        # strating at the one closest to end
        for p, s in pairs:
            # calculate how fast we get to target
            dist = target-p
            rate = float(dist)/s
            stack.append(rate)
            if stack and len(stack)>=2 and stack[-1] <= stack[-2]:

                stack.pop()

        return len(stack)
  
