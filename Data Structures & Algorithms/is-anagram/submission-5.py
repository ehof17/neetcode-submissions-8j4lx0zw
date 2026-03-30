class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c_s = {}
        c_t = {}
        for c in s:
            c_s[c] = c_s.get(c, 0) + 1
        for c in t:
            c_t[c] = c_t.get(c,0)+1
        return c_s==c_t
        
