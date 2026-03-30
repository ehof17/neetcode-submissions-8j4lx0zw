class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        # partition the array into 2 equal halves
        total_el = len(nums1) + len(nums2)
        half = total_el // 2

        if len(B) < len(A):
            A, B = B, A

        # get half of the elements of one
        L, R = 0, len(A) - 1

        # default that there is pos inf in small
        while True:
            
            mid_a  = (L+R) // 2
            mid_b = half - mid_a - 2

            Aleft = A[mid_a] if mid_a >= 0 else float('-infinity')
            Aright = A[mid_a+1] if (mid_a + 1) < len(A) else float('infinity')
            Bleft = B[mid_b] if mid_b >= 0 else float('-infinity')
            Bright = B[mid_b+1] if (mid_b + 1) < len(B) else float('infinity')



            if Aleft <= Bright and Bleft <= Aright:
                if total_el % 2 == 0:
                    # max of left and min of left
                    maxV = max(Aleft, Bleft)
                    minV = min(Aright, Bright)
                    median = (maxV + minV) / 2
                else:
                    median = min(Aright, Bright)
                return median

            
            elif Aleft > Bright:
                R = mid_a - 1
            else:
                L = mid_a + 1

            
            # how can we determine how ALL things in the left are less than the right
            # the partion is both arrays

            # is the rightmost in the left less than the left in the other array


