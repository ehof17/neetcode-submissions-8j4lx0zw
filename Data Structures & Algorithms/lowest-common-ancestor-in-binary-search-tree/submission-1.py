# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # If p and q are in different subtrees
        # we are LCA
        if p.val < root.val < q.val or q.val < root.val < p.val:
            return root
        # otherwise if p and q are in subtrees
        # The LCA is in that subtree
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)

        return root
        # p root q
        # q root p
        # root q p
        # p q root

       