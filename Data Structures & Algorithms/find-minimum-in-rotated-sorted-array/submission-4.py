class Solution:
    def findMin(self, nums: List[int]) -> int:
        L = 0
        R = len(nums) - 1
        minVal = nums[L]
        while L <= R:
         
            # since here it is sorted
            if nums[L] < nums[R]:
                minVal = min(minVal, nums[L])
                break
            M = (L+R) // 2
            minVal = min(minVal, nums[M]) 
            if nums[L] <= nums[M]:
                L = M + 1

            else:
                R = M - 1

        return minVal
        

            

            


      
        
       
            

        