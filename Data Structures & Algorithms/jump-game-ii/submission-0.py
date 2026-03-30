class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        L = R = 0

        while R < len(nums)-1:
            furthest = 0
            for i in range(L, R+1):
                furthest = max(furthest, i + nums[i])
            L = R+1
            R = furthest
            res+=1
        return res
