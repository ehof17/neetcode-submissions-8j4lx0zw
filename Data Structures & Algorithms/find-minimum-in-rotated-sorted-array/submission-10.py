class Solution:
    def findMin(self, nums: List[int]) -> int:
        L = 0
        R = len(nums)-1
        minVal = nums[0]
        while L < R:
            mid = (L + R) // 2
            minVal = min(minVal, nums[L])
            minVal = min(minVal, nums[R])
            minVal = min(minVal, nums[mid])
            # if mid is greater than left
            # 3, 4, 1, 2, 2, 2, 2, 2, 3
            # is that always our minVal?
            # We are either the minVal, or the minVal is to the left

            # if mid is greater than right
            # we should Search right 
            # 
            # 1,2,3,4,5,6,1
            print(f"L: {L}, R:{R}, mid:{mid}")

            print(f"MIDVAL {nums[mid]}, LVAL: {nums[L]}, RVAl: {nums[R]}")
            if nums[mid] > nums[L]:
                if nums[R] < nums[L]:
                    print("searchin right half")
                    L = mid
                else:
                    print("Searchin left half")
                    print(f"nums[mid], {nums[mid]} > nums[L]: {nums[L]}")
                    R = mid
            elif nums[mid] > nums[R]:
                print("Searchin right half")
                print(f"nums[mid], {nums[mid]} > nums[R]: {nums[R]}")
                L = mid + 1
           # elif nums[mid] < nums[L]:
           # if midVal is smaller than Lval or RVal
           # would we have to check both
           # maybe just go left
           # 
           # 3,4,1,2,2,2,2

            else:
                print("checkin min then searchin left half")
                minVal = min(minVal, nums[mid])
                R = mid

        return minVal



      
        
       
            

        