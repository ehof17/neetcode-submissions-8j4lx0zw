# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0,next=head)
        # if we have a group
        # 1 -> [2 -> 3]
        # we need previous of the group
        # to eventaully point its next pointer
        # 1 -> [3 -> 2]
        groupPrev = dummy
        while True:
            # If we are at the end
            kth = self.get_Kth(groupPrev, k)
            if not kth:
                break
            # first item in next group
            nxt_first = kth.next
            # first item in current group
            curr = groupPrev.next
            # cant assign prev to None
            # since that will break the list
            # instead we need to assign to next
            prev = kth.next
            # [1->2] -> (3)
            # prev = 3
            # [2->1->3]

            # reverse the list
            while curr and curr != nxt_first:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            # x->0->1->2->3
            originalFirst = groupPrev.next # 0
            # x->0<-1
            #    |
            #    v
            #    2->3
            groupPrev.next = kth  # x->1->0->2->3
       
            groupPrev = originalFirst # x->1->[0]->2->3
            
            
        return dummy.next
    def get_Kth(self, curr, k):
        cnt =0 
        while curr and cnt < k:
            nxt = curr.next
            cnt+=1
            curr = nxt
        return curr
        

        



       