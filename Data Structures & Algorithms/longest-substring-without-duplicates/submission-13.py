from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Expand until we are at the target
        L,R = 0,0
        charSet = set()
        maxNum = 0
        for R in range(len(s)):
            while s[R] in charSet:
                charSet.remove(s[L])
                L+=1
            charSet.add(s[R])
            curNum = R - L + 1
            maxNum = max(maxNum, curNum)


        return maxNum

        