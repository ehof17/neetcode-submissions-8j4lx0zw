class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        needed_cnts = {}
        for c in t:
            needed_cnts[c]  = needed_cnts.get(c, 0) + 1
        
        # 1: Find the window of all
        L = 0
        res = ""
        minLen = float('infinity')
        for R in range(len(s)):
            if s[R] in needed_cnts:
                needed_cnts[s[R]]-=1
            if all(val <= 0 for val in needed_cnts.values()):
                print(f"we got all weneed R is {R} L is {L}")
        
                while L < R and needed_cnts.get(s[L], float('-infinity')) < 0:
                    if (R-L+1) < minLen:
                        res = s[L:R+1]
                        minLen = min(minLen, R-L+1)
                    if s[L] in needed_cnts:
                        needed_cnts[s[L]]+=1
                    L+=1
                if (R-L+1) < minLen:
                    res = s[L:R+1]
                    minLen = min(minLen, R-L+1)
                # here im only incrementing by 1
                if s[L] in needed_cnts:
                    needed_cnts[s[L]]+=1
                    L+=1
                # l is only updated if we got all we need



        # 2: Shrink it
        return res
