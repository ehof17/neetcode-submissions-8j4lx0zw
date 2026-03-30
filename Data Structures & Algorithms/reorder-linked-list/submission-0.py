# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # first, last, second, second to last

        # just weave it
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # mid = slow
        # reverse mid to end
 
        prev = None
        rev = slow.next
        slow.next = None
        while rev:
            temp = rev.next
            rev.next = prev
            prev = rev
            rev = temp
        first, second = head, prev

        while second:
            temp_f = first.next
            temp_s = second.next
            first.next = second
            second.next = temp_f
            first, second = temp_f, temp_s
        #first.next.next = temp.next

        


        #return first
       
        
      

