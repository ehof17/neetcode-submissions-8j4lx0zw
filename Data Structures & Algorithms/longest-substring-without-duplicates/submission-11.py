class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        L = 0
        maxLen = 0
        charSet = set()
        for R in range(len(s)):
            while s[R] in charSet:
                charSet.remove(s[L])
                L+=1
            charSet.add(s[R])
            curLen = R - L + 1
            maxLen = max(maxLen, curLen)
        return maxLen

                

            
