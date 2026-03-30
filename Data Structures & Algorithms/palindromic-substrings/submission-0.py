class Solution:
    def countSubstrings(self, s: str) -> int:
        # start with individual letters
        res = len(s)
        for i in range(len(s)):
            L = i
            R = i

            L-=1
            R+=1

            while L >=0 and R < len(s) and s[L] == s[R]:
                res+=1
                L-=1
                R+=1

        for i in range(len(s)):
            L = i
            R = i

            R+=1

            while L >=0 and R < len(s) and s[L] == s[R]:
                res+=1
                L-=1
                R+=1
        return res

        

        
            
