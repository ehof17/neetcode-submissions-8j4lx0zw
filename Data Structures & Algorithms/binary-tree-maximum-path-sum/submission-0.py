# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # at a node, if the curSum = negative, curSum actually equals curVal
        # then pass currSum
        res = [root.val]
        maxVal = float('-infinity')
        def dfs(node):
            if not node: return 0

            # 3 scenarios
            # left and right subtree, current node connects
            # only left or only right
            # Another considers the path extending from currentNode to parent
            lftmax = max(dfs(node.left), 0)
            rightmax = max(dfs(node.right), 0)
            res[0] = max(res[0], node.val + lftmax + rightmax)
            return node.val + max(lftmax, rightmax)
        dfs(root)
        return res[0]

        
