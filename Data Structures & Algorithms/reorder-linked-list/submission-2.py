# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # slow is now the left half
        # 1 2 3 4 5
        # S F
        #   S   F
        #.    S    F
        # 1 2 3 4
        # S F
        #   S   F
        rev = slow.next
        prev = slow.next = None
        curr = rev
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        l1, l2 = head, prev
        while l2:
            t_hn, t_pn = l1.next, l2.next
            l1.next = l2
            l2.next = t_hn
            l2 = t_pn
            l1 = t_hn



    


        