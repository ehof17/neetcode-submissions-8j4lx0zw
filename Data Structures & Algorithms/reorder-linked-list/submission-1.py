# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # 0.next = n
        # n.next = 0.next (but prev)
        # n.1
        fast, slow = head.next, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # slow is now pointing to mid point
        # second half needs to be reversed and merged
        second = slow.next
        prev = slow.next = None
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        # prev is reversed list

        l1 = head
        l2 = prev

        # l1.next = prev
        #  
        while l2:
            tmp_l1_next, tmp_l2_next = l1.next, l2.next
            l1.next = l2
            l2.next = tmp_l1_next
            l1 = tmp_l1_next
            l2 = tmp_l2_next
        



    


        