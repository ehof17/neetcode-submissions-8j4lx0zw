class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        box = set()
        for i in nums:
            if i in box:
                return True
            else:
                box.add(i)
        return False
         