# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        
        if self.isSame(root, subRoot):
            return True

        val = (
            self.isSubtree(root.right, subRoot) or
            self.isSubtree(root.left, subRoot)
        )
        return val

        




    def isSame(self, q, p):
        if not q and not p:
            return True

        if q and not p:
            return False

        if p and not q:
            return False

        if q.val == p.val and self.isSame(p.left, q.left) and self.isSame(p.right, q.right):
            return True

        return False
        