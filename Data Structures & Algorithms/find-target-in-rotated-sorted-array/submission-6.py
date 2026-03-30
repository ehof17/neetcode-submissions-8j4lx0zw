class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L,R = 0, len(nums)-1
        while L <=R:
            M = (L+R) // 2
            if nums[M] == target:
                return M
            # if M is in left or right

            # in left
            if nums[M] >= nums[L]:
                # if out of bounds, search right
                if nums[L] > target:
                    L = M+1
                # if too small search right
                elif nums[M] < target:
                    L = M + 1
                else:
                    R = M - 1
            else:
                # if out of bounds, search left
                if nums[R] < target:
                    R = M - 1
                elif nums[M] > target:
                    R = M - 1
                else:
                    L = M +1

                # if

        return -1
        