class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # while s[R] not in curSet:
        # add s[R]
        maxLen = 0
        L = 0
        curSet = set()
        for R in range(len(s)):
            while L <= R and s[R] in curSet:
                curSet.remove(s[L])
                L+=1

            maxLen = max(maxLen, R-L+1)
            curSet.add(s[R])
        return maxLen
        

                


