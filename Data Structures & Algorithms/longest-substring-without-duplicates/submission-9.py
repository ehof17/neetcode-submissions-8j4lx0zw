class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        maxLen = 0
        L = 0
        # grow the window until it has a repeated char
        # then start moving left pointer
        for R in range(len(s)):

            while s[R] in chars:
                chars.remove(s[L])
                L+=1

            chars.add(s[R])
            maxLen = max(maxLen, R-L+1)
        return maxLen

