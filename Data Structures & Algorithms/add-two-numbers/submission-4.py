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
            val1 = curr.val if curr else 0
            val2 = curr2.val if curr2 else 0
            sums = val1+val2
            sums+=carry
            carry, val = divmod(sums, 10)
            head2.next = ListNode(val)
            head2 = head2.next

            curr = curr.next if curr else None
            curr2 = curr2.next if curr2 else None
        return head.next



            


       