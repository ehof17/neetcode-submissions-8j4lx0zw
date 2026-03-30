class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
       # for each number
       # we need to find 2 numbers to the right that sum to the number
       # so we only need to check if the number 
        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # else we are here
            L = i+1
            R = len(nums)-1
            while L < R:
                curSum = num + nums[L] + nums[R]
                if curSum > 0:
                    R -=1
                elif curSum < 0:
                    L+=1
                # we found match
                else:
                    res.append([num, nums[L], nums[R]])
                    L+=1
                    R-=1
                    while (nums[L] == nums[L-1] and L < R):
                        L+=1

        return res