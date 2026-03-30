class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        maxLen = 0
        L = 0
        for i in range(len(s)):
            char = s[i]
            while char in chars:
                chars.remove(s[L])
                L+=1
            maxLen = max(maxLen, i-L+1)
            chars.add(char)

        return maxLen

