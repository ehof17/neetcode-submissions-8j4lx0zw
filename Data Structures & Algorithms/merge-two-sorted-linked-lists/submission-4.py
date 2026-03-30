# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        
        l1p = list1
        l2p = list2

        if l1p and not l2p:
            minVal = l1p.val
            l1p = l1p.next

        elif l2p and not l1p:
            minVal = l2p.val
            l2p = l2p.next

        elif l1p.val < l2p.val:
            minVal = l1p.val
            l1p = l1p.next
        else:
            minVal = l2p.val
            l2p = l2p.next

        res = ListNode(minVal)
        head = res
        while l1p and l2p:
            if l1p.val < l2p.val:
                # next is l1p
                res.next = l1p
                l1p = l1p.next

            else:
                res.next = l2p
                l2p = l2p.next
            res = res.next

        while l1p:
            res.next = l1p
            res = res.next
            l1p = l1p.next
        
        while l2p:
            res.next = l2p
            res = res.next
            l2p = l2p.next

        return head
