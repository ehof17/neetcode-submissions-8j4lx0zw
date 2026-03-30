class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count1 = {}
        count2 = {}
        for c in s:
            count1[c] = 1 + count1.get(c, 0)
        for c in t:
            count2[c] = 1 + count2.get(c,0)
        return count1==count2
