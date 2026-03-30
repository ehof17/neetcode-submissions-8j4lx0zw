class Solution:
    def findMin(self, nums: List[int]) -> int:
        # need to go to right arr
        minVal = nums[0]
        L, R = 0, len(nums)-1
        while L <= R:
            minVal = min(minVal, nums[L])
            M = (L+R) //2
            minVal = min(minVal, nums[M])
            if nums[M] >= nums[L]:
                # M is in left
                L = M + 1
            else:
                R = M - 1

        return minVal

        