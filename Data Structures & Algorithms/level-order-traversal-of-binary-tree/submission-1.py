# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque, defaultdict

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        res = defaultdict(list)
        queue = deque()
        queue.append((root, 0))
        while queue:
            p, lvl = queue.popleft()
            if p.left:
                queue.append((p.left, lvl+1))
            if p.right:
                queue.append((p.right, lvl+1))
            res[lvl].append(p.val)
        return list(res.values())
        