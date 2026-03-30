from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Expand until we are at the target
        L = 0
        R = 0
        length = 0
        charSet = set()
        for R in range(len(s)):
            while s[R] in charSet:
                charSet.remove(s[L])
                L+=1
            charSet.add(s[R])
            length = max(length, R - L + 1)
            
        return length

        