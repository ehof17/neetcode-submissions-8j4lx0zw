# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def dfs(node):
            if not node:
                return [True, 0]

            left = dfs(node.left) 
            right = dfs(node.right) 
            leftval = left[1]
            rightval = right[1]
            
            balancedval = abs(rightval - leftval) == 0 or abs(rightval - leftval) == 1
            balanced = balancedval and left[0] and right[0]


            return [balanced, 1+ max(leftval, rightval)]

        return dfs(root)[0]



            