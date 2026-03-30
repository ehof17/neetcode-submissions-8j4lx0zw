# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        queue = []
        valcue = []
        if root:
            queue.append(root)
            valcue.append(root.val)
        while queue:
            res.append(valcue.copy())
            for i in range(len(queue)):
                curr = queue.pop(0)
                valcue.pop(0)
                if curr.left:
                    queue.append(curr.left)
                    valcue.append(curr.left.val)
                if curr.right:
                    queue.append(curr.right)
                    valcue.append(curr.right.val)
        return res

        
        