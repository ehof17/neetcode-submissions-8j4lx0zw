# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_visited):
            if not node:
                return 0
            count = 1 if node.val >= max_visited else 0
            max_visited = max(max_visited, node.val)
            count += dfs(node.left, max_visited)
            count += dfs(node.right, max_visited)
            return count

        return dfs(root, float('-inf'))