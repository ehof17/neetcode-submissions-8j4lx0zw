# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # if child is greater then it is a good node
        # chils must be greater than the root
        # it is the max Value
        count = 1
        def dfs(maxV, node):
            if not node:
                return 0
            res = 1 if node and node.val >= maxV else 0
            maxV = max(node.val, maxV)
            res += dfs(maxV, node.right)
            res += dfs(maxV, node.left)
            return res

        return dfs(root.val, root)