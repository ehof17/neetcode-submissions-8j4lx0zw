class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # once its in a fleet then it is in forever
        pairs = [(pos, s) for pos, s in zip(position, speed)]
        pairs.sort(reverse=True)
        stack = []
        for p, s in pairs:
            calc = (target-p)/s
            stack.append(calc)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)