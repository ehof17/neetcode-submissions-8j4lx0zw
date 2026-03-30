from collections import Counter, defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        L, R = 0, len(s1)
        cnt_s1 = [0] * 26
        cnt_val = [0] * 26
        for c in s1:
            cnt_s1[ord(c) -ord('a')] +=1
  
        for i in range(len(s1)):
            cnt_val[ord(s2[i])-ord('a')]+=1

        while R < len(s2):
            print(cnt_val)
            if cnt_val == cnt_s1:
                return True
            
            cnt_val[ord(s2[R]) - ord('a')]+=1
            cnt_val[ord(s2[L]) - ord('a')]-=1

            R+=1
            L+=1
        return cnt_val == cnt_s1