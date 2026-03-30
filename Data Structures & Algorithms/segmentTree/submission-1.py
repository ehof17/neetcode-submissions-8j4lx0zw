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

        root = TreeNode(0, L, R)
        M = (L + R) // 2
        root.left = self.build(nums, L, M)
        root.right = self.build(nums, M+1, R)
        root.sum = root.right.sum + root.left.sum
        return root
            

    def update(self, idx, val):
        self.update_r(self.root, idx, val)

    def update_r(self, root, idx, val):
        if root.L == root.R:
            root.sum = val
            return
        
        M = (root.L+root.R) // 2

        if idx > M:
            self.update_r(root.right, idx, val)
        else:
            self.update_r(root.left, idx, val)
        root.sum = root.right.sum + root.left.sum

    def query(self, L, R):
        return self.query_r(self.root, L, R)

    def query_r(self, root, L, R):
        if root.L == L and root.R == R:
            return root.sum
        
        M = (root.L+root.R) // 2
        if M < L:
            return self.query_r(root.right, L, R)

        elif M >= R:
            return self.query_r(root.left, L, R)

        else:
            return(self.query_r(root.left, L, M) + self.query_r(root.right, M+1, R))


        



     