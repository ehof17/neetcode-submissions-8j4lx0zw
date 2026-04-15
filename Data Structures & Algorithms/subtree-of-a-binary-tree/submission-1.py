# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque 
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # at any point
        # go trrough root
        queue = deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if self.isSameTree(node, subRoot):return True
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return False
        

    def isSameTree(self, node1, node2):
        if not node1 and not node2: return True
        if node1 and not node2: return False
        if node2 and not node1: return False
        if node2.val != node1.val: return False
        left = self.isSameTree(node1.left, node2.left)
        right = self.isSameTree(node1.right, node2.right)
        return left and right