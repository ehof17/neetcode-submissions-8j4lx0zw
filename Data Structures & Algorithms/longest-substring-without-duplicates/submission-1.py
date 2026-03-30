class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0
        length = 0
        chars = set()
        for R in range(len(s)):
            while s[R] in chars:
                chars.remove(s[L])
                L+=1
            chars.add(s[R])
            length = max(length, R - L + 1)
            
        return length
