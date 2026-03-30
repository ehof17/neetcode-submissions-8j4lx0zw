class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return ["()"]
        # gonna have n opening and closing parenthesis
        # after opening you can close it
        # or open another
        # if the count is less than  n
        opens = 0
        curr = ""
        res = []
        def dfs(opens, closes, curr):
            if (opens == closes == n):
                if curr not in res:
                    res.append(curr)
                return
            if len(curr) == 2*n:
                return
                

       
            # path with another open
            if opens < n and len(curr) < 2*n-1:
                dfs(opens+1, closes, curr+"(")
                

            # path with a closing
            if opens >= 1 and opens > closes:
                dfs(opens, closes+1, curr+")")
                
        dfs(1,0,"(")
        return res

        
            

        