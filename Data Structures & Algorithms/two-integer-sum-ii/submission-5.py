class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # get a map
        L, R = 0, len(numbers)-1
        while L < R:
            curSum = numbers[L] + numbers[R]
            if curSum == target:
                return [L+1, R+1]
            if curSum > target:
                R-=1
            elif curSum < target:
                L+=1
        
        
       
      