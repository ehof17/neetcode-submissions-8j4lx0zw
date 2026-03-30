class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        L = 0
        R = len(nums)-1
        res = []
        nums = sorted(nums)
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue
            L, R = i +1, len(nums) -1
            while L < R:
                t_sum = a + nums[L] + nums[R]
                if t_sum > 0:
                    R-=1
                elif t_sum < 0:
                    L+=1
                else:
                    res.append([nums[L], nums[R], a])
                    L+=1
                    while L < R and nums[L] == nums[L-1]:
                        L+=1
                   
        return res