class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        # partition the array into 2 equal halves
        total_el = len(nums1) + len(nums2)
        half = total_el // 2

        if len(B) < len(A):
            A, B = B, A

        
        L, R = 0, len(A) - 1
        while True:
            
            M = (L+R) // 2
            M_B = half - M - 2
            # No guarantee that M is in the left
            # now we need to check against one another
            A_left = A[M] if M >= 0 else float('-infinity')
            B_left = B[M_B] if M_B >= 0 else float('-infinity')

            A_next = A[M+1] if len(A) > M+1 else float('infinity')
            B_next = B[M_B+1] if len(B) > M_B+1 else float('infinity')
            
            # we got our parition
            if A_left <= B_next and B_left <= A_next:
                # if even
                if total_el %2 == 0:
                    mx_1 = max(A_left, B_left)
                    mn_1 = min(A_next, B_next)
                    return (mx_1 + mn_1) / 2
                    
                else:
                    return min(A_next, B_next)

            elif A_left > B_next:
                # need to remove A_left from part
                # and add B_next to it
                R = M-1
            elif B_left > A_next:
                # need to remvove B_left from part
                # and add A_next to it
                L = M+1
        
       