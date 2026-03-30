class Solution:
    def findMin(self, nums: List[int]) -> int:
        L = 0
        R = len(nums)-1
        # 2 of l, mid, and r will be in the same sorted segment
        # find the place where they are not in increasing order
        # Consider 
        minVal = nums[L]
        while L <= R:
            mid = (L+R) // 2
            if nums[L] < nums[R]:
                minVal = min(minVal, nums[L])
            minVal = min(minVal, nums[mid])
            # Are we in the left sorted portion or left portion
            # If we are in the left, we want to sort the right
            # Since if we rotated the array, everything will be greater
            # 
            # check if mid >= L
            # This means we are in the Right portion
            if nums[mid] >= nums[L]:
                L = mid + 1
            else: 
                R = mid - 1
        return minVal

            # if we are in the right sorted portion
            # Then we want to search to the left


        

            

            


      
        
       
            

        