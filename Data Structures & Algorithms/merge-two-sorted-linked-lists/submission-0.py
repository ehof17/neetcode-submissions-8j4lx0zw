# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2
 
        hm = ListNode()
        head = hm

        while (curr1 and curr2):
            if curr1.val > curr2.val:
                head.next = ListNode(curr2.val)
            # if we add curr1
                curr2 = curr2.next
            else: 
            
                head.next = ListNode(curr1.val)
                curr1 = curr1.next
            head = head.next

        if curr1:
            while (curr1):
                head.next = ListNode(curr1.val)
                curr1 = curr1.next
                head = head.next
        while curr2:
            head.next = ListNode(curr2.val)
            curr2 = curr2.next
            head = head.next

        return hm.next
        