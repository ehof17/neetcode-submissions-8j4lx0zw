class Solution:
    def search(self, nums: List[int], target: int) -> int:
        res = -1
        L = 0
        R = len(nums)-1

        while L <= R:
            mid = (L+R) // 2
            print(mid)
            if nums[mid]==target: return mid

            if nums[L] <= nums[mid]:
                # left is sorted
                if nums[L] <= target < nums[mid]:
                    print("update R 1")
                    R = mid -1
                else:
                    print("update L 1")
                    L = mid + 1

            else:
                # right is sorted. 
                if nums[mid] <= target <= nums[R]:
                    print("update L2")
                    L = mid + 1
                else:
                    print("update R2")
                    R = mid -1


           
        return res