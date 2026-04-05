class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
       res = []
       nums.sort()
       for i, num in enumerate(nums):
        # Distinct
        if i > 0 and num == nums[i-1]:
            continue
        target = -num
        L = i+1
        R = len(nums)-1
        while L < R:
            if nums[L] + nums[R] > target:
                R-=1
            elif nums[L] + nums[R] < target:
                L+=1
            else:
                res.append([nums[i], nums[L], nums[R]])
                # no dupes..
                L+=1
                while  L<R and nums[L] == nums[L-1]:
                    L+=1
                R-=1

       return res