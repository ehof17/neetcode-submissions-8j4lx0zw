# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]
        def dfs(node):
            if not node: return 0
            lftmax = dfs(node.left)
            lftmax = max(lftmax, 0)
            rightmax = dfs(node.right)
            rightmax = max(rightmax, 0)

            # if WE DO split here, we can add up everything
            res[0] = max(res[0], node.val + lftmax + rightmax)

            # return as if we didn't split here tho
            return node.val + max(lftmax, rightmax)

        dfs(root)
        return res[0]