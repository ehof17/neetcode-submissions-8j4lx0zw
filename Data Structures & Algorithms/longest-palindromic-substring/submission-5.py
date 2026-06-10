class Solution:
    def longestPalindrome(self, s: str) -> str:
        # look at every character, if it is a palindrome continue updating and expand out
        if len(s) == 1:
            return s
        res = s[0]
        maxLen = 1
        L = 0
        R = 0
        # Expand outward from char
        for i in range(len(s)):
            L = i
            R = i
            if L < 0 or R >= len(s):
                continue
            L-=1
            R+=1
            
            
            while L >= 0 and R < len(s) and s[L] == s[R]:
                potres = s[L:R+1]
               
                if len(potres)>len(res):
                    res = potres
                L-=1
                R+=1
                
        for i in range(len(s)):
            L = i
            R = i
            
            R+=1
    

            while L >= 0 and R < len(s) and s[L] == s[R]:
               # print("yes")
                potres = s[L:R+1]
                if len(potres)>len(res):
                    res = potres
                L-=1
                R+=1
        
    
        return res
           