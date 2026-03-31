# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # val + val
        # curVal1 + curVal2 + remainder from last
        # len(l1) doesnt need to be len(l2)
        dummy = ListNode()
        head = dummy
        head2 = dummy
        curr, curr2 = l1, l2

        carry = 0
        while curr or curr2 or carry:
            hm = curr.val if curr else 0
            hm2 = curr2.val if curr2 else 0

            currSum = hm+hm2 + carry
            carry, newval = divmod(currSum, 10)

            newNode = ListNode(newval)
            head2.next = newNode
            head2 = head2.next
 
            curr = curr.next if curr else None
            curr2 = curr2.next if curr2 else None
         

        return head.next


            


       