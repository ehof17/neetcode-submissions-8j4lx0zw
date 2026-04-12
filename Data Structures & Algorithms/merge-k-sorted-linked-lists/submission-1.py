# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        
        # merge2 lists[0] lists[1]

        START, END = 0, 1
        startNode, endNode = lists[START], lists[END]
        merged = self.mergeTwo(startNode, endNode)
        i = 2

        while i < len(lists):
            merged = self.mergeTwo(merged, lists[i])
            i+=1
        # then we gotta merge with every other one bruh
        return merged

        

    def mergeTwo(self, l1, l2):
        dummy = ListNode()
        tail = dummy
        while l1 and l2:
            l1val = l1.val
            l2val = l2.val
            if l1val < l2val:
                tail.next = l1
                l1 = l1.next
                tail = tail.next
            else:
                tail.next = l2
                l2 = l2.next
                tail = tail.next


        while l1:
            tail.next = l1
            tail = tail.next
            l1 = l1.next

        while l2:
            tail.next = l2
            tail = tail.next
            l2 = l2.next

        return dummy.next