# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        head = dummy
        while list1 and list2:
            v1 = list1.val
            v2 = list2.val
            if v1 < v2:
                head.next = list1
                list1 = list1.next
                head = head.next
            else:
                head.next = list2
                list2 = list2.next
                head = head.next
        while list1:
            head.next = list1
            list1 = list1.next
            head = head.next
        while list2:
            head.next = list2
            list2 = list2.next
            head = head.next
        return dummy.next
