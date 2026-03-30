from collections import defaultdict
class Solution:
   
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        window_len = len(s1)
        s1Map = defaultdict(int)
        s2Map = defaultdict(int)
        alph="abcdefghijklmnopqrstuvwxyz"
        # total num of equal chars in each hash
        # if s1 count matches s2 matches
        # solution will have 26 matches
        # abc
        # baxyzabc
        # abc has 26 matches with the other window, there is 0
        matches = 0

        for i in s1:
            s1Map[i]+=1
        L = 0

        for i in range(window_len):
            s2Map[s2[i]]+=1
        
        for i in alph:
            if s1Map[i] == s2Map[i]:
                matches+=1
        print(matches)
        for R in range(window_len, len(s2)):
            if matches == 26:
                return True
            s2Map[s2[R]] +=1
            #if they are now equal
            if s1Map[s2[R]] == s2Map[s2[R]]:
                matches+=1
            # They were equal previously
            elif s1Map[s2[R]]+1 ==s2Map[s2[R]]:
                matches -=1

            s2Map[s2[L]] -=1
            #if they are now equal
            if s1Map[s2[L]] == s2Map[s2[L]]:
                matches+=1
            # They were equal previously
            elif s1Map[s2[L]] - 1 ==s2Map[s2[L]]:
                matches -=1
            L+=1
        return matches==26


                
                

        