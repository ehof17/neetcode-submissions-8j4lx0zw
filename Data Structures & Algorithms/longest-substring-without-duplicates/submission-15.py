class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        L,R=0,0
        curSet = set()
        while R < len(s):
            
            while s[R] in curSet:
                curSet.remove(s[L])
                L+=1
            curSet.add(s[R])
            maxLen = max(maxLen, len(curSet))
            R+=1
        return maxLen
        

                


