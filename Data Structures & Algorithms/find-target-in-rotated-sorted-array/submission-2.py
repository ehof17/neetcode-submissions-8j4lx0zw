class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L = 0
        R = len(nums) -1

        minIndex = -1

        # just need to find the pivot

        while L <= R:
            M = (L+R) // 2
            if nums[M] == target:
                return M

            # left half may be sorted
            # 1,2,3,4,5,6
            # L.  M
            # could left half ever not be sorted?
            # 5,1,2,3,4
            #   L    R

            # if the target is less than the lowest value
            # in one of the halves
            # then we know we don't need to search

            if nums[M] >= nums[L]:
                # mid val belongs to left sorted portion
                if nums[L] <= nums[M]:
                    # we have to search right
                    # if L is too big
                    # or tar
                    if target > nums[M] or target < nums[L]:
                        # search right portion
                        L = M+1
                    # if not true
                    # target is less than middle
                    # but greater than left
                    else:
                        # search left portion
                        R = M -1

            else:
                # right sorted portion
                
                # if mid bigger
                # or target too big of right
                if target < nums[M] or target > nums[R]:
                    R = M - 1

                # target is greater than middle
                # and target less than right
                else:
                    L = M + 1

        return -1