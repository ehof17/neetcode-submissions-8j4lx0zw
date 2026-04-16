# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque, defaultdict
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # only go right 
        # nope
        # at every level, get the right most val
        # 
        if not root: return []
        lvl_cnts = defaultdict(list)
        queue = deque()
        queue.append((root, 0))
        while queue:
            n, lvl = queue.popleft()
            # if we process the left first
            # we would just have to get the LAST value at each level
            if n.left:
                queue.append((n.left, lvl+1))
            if n.right:
                queue.append((n.right, lvl+1))
            lvl_cnts[lvl].append(n.val)
        res = []
        for k,v in lvl_cnts.items():
            res.append(v[-1])
        return res