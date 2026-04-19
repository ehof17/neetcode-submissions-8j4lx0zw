# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # unique values
        # In order is left most
        # preOrder is BFS
        # root is always going to be inOrder[0]
        # then we will have a max of 2^level nodes
        # How do we know that its not 
        # 1
        # 2 3
        # 4
        # and it is actually
        # 1
        # 2 3
        #    4
        #: using the preorder tree
    
        rootVal = preorder[0]
        root = TreeNode(rootVal)
        inOrderIdxMap = {}
        for i, node in enumerate(inorder):
            inOrderIdxMap[node]=i
        self.pre_idx = 0

        def dfs(l,r):
            if l > r: return None
            val = preorder[self.pre_idx]
            self.pre_idx+=1
            node = TreeNode(val)
            mid = inOrderIdxMap[val]
            node.left = dfs(l, mid-1)
            node.right = dfs(mid+1, r)
            return node
   
        return dfs(0, len(preorder)-1)

        #  1
        # 2
        #  3
        # we know root.left OR root.right OR both will be preOrder[1:2]
        # 
        # split in half
        

      

    