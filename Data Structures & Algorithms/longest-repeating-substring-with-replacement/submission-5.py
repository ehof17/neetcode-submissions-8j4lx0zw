from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = defaultdict(int)
        L = 0
        R = 0
        charSet = set(s)
        maxCount = 0
        for c in charSet:
            L = count_num = 0
            for R in range(len(s)):
                if s[R] == c:
                    count_num+=1
                
                while (R-L+1) - count_num > k:
                    if s[L] == c:
                        count_num-=1
                    L+=1
                maxCount = max(maxCount, R-L+1)

        return maxCount
                

        