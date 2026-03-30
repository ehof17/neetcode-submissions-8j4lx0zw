class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L = 0
        R = len(nums) -1
        while L <= R:
            M = (L+R) // 2
            if nums[M] == target:
                return M
            # are we in left pivot?
            if nums[L] <= nums[M]:
                # need to search to the right
                # if smallest val is too big
                # or mid is too small
                if nums[L] > target or nums[M] < target:
                    L = M + 1
                else:
                    R = M - 1
            # in right pivot
            else:
                if nums[R] < target or nums[M] > target:
                    R = M - 1
                else:
                    L = M + 1

        return -1
