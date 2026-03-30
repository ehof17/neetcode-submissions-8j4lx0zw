from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # window size = len(s1)
        if s1 == s2:
            return True
        WINDOW_LEN = len(s1)
        print(WINDOW_LEN)
 
        L = 0
        R = WINDOW_LEN
        while R < len(s2) + WINDOW_LEN -1:  
            print(f"L is {L} and R is {R}")
            if sorted(s2[L:R]) == sorted(s1):
                return True
            print(s2[L:R])
            L+=1
            R+=1
        return False
        