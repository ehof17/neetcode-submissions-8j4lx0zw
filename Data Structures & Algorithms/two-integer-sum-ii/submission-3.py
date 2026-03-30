class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # get a map
        L = 0
        R = len(numbers) - 1
        # if too big, move R bacl
        # if too small, move L forwar
        while L < R:
            curSum = numbers[L] + numbers[R]
            if curSum > target:
                R-=1
            elif curSum < target:
                L+=1
            else:
                return [L+1, R+1]


        
       
      