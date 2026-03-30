class Solution:
    def numDecodings(self, s: str) -> int:
        # 1 or 2
        # check using the 1 and using the next char as 
        # prev char is 1 -> next can be 0 - 9
        # prev char is 2 -> next can be 0 - 6
        valid_after_6 = ["0","1","2","3","4","5","6"]
        def dfs(i):
            if i == len(s):
                return 1
            
            if s[i] == '0':
                return 0

            res = dfs(i+1)
            if i < len(s) -1:
            
                if s[i] == "1" or s[i] == "2" and s[i+1] in valid_after_6:
                    res+= dfs(i+2)

                    

            return res
    
        return dfs(0)
       
            
            
