class Solution:
    def findMin(self, nums: List[int]) -> int:
        L = 0
        R = len(nums) - 1
        minVal = nums[L]
        while L <= R:
            if nums[L] < nums[R]:
                minVal = min(minVal, nums[L])
                break

            M = (L+R) // 2
            minVal = min(minVal, nums[M])
            # we are in left, search right
            if nums[M] >= nums[L]:
                L = M+1
            # we are in right, search left
            else:
                R = M - 1

        return minVal


      
        
       
            

        