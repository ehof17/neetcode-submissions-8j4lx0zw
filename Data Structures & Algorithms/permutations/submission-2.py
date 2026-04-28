

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]
        for n in nums:
            new_perms = []
            for p in perms:
                for i in range(len(p)+1):
                    pcop = p.copy()
                    pcop.insert(i,n)
                    new_perms.append(pcop)
            perms = new_perms
        return perms