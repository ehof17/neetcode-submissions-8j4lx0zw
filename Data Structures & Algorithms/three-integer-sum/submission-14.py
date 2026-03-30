class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        L = 0
        for i, num in enumerate(nums):
            if i > 0 and nums[i-1] == num:
                continue
            
            L = i + 1
            R = len(nums) -1
            while L <  R:
                curSum = num + nums[L] + nums[R]
                if curSum > 0:
                    R-=1
                elif curSum < 0:
                    L+=1
                else:
                    res.append([num, nums[L], nums[R]])
                    L+=1
                    R-=1
                    while (L < R and nums[L] == nums[L-1]  ):
                        L+=1
                

            


        return res