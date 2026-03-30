class TreeNode:
    def __init__(self, total, L, R):
        self.sum = total
        self.left = None
        self.right = None
        self.L = L
        self.R = R

class SegmentTree:
    
    def __init__(self, nums: List[int]):
        self.root = self.build(nums, 0, len(nums) -1)


    def build(self, nums, L, R):
        if L == R:
            return TreeNode(nums[L], L, R)
        M = (L + R) // 2
        root = TreeNode(0,L,R)
        root.left = self.build(nums, L, M)
        root.right = self.build(nums, M+1, R)
        root.sum = root.left.sum + root.right.sum
        return root

    
    def update(self, index: int, val: int) -> None:
        self.update_r(self.root, index, val)

    def update_r(self, root, index, val):

        if root.L == root.R:
            root.sum = val
            return
        M = (root.L + root.R) //2
        if index > M:
            self.update_r(root.right,index,val)
        else:
            self.update_r(root.left,index,val)
          
        root.sum = root.left.sum + root.right.sum

    
    def query(self, L: int, R: int) -> int:
        return self.query_r(self.root, L, R)

    def query_r(self, root, L, R):
        if L == root.L and R == root.R:
            return root.sum
        M = (root.L + root.R) //2
        if L > M:
            return self.query_r(root.right, L, R)
        elif R <= M:
            return self.query_r(root.left, L, R)

        else:
            return ( self.query_r(root.left,L,M) + self.query_r(root.right, M+1, R))



