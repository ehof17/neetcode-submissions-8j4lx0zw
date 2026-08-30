class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        numcnt = {}
        target = len(nums) / 2
        for num in nums:
            if num in numcnt:
                numcnt[num]+=1
                if numcnt[num] >= target:
                    return num
            else:
                numcnt[num]=1
        