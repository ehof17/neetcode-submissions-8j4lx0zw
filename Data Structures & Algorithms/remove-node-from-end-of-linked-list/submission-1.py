# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = dummy
        for _ in range(n):
            right = right.next
        # 1 2 3 4 5
        # 3
        #.    x
        #   R R R
        # L
        #   L.    R
        #.    L.    x
        prev = left
        while right:
            prev = left
            left = left.next
            right = right.next
        
        # left is now pointing to what we want out
        # skip over it
        prev.next = left.next
        return dummy.next
        


        
        