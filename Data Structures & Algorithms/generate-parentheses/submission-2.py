class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return ["()"]
        # gonna have n opening and closing parenthesis
        # after opening you can close it
        # or open another
        # if the count is less than  n
        # max amount of opens is n
        opens = 0
        curr = ""
        res = []
        def dfs(opens, closes, string):
            if opens == closes == n:
                res.append(string)
                return
            
            # if the amount of opens isn't n yet we can add
            if opens < n:
                dfs(opens+1, closes, string+"(")

            # when do we add a close
            # if opens > closes and opens+closes < n
            if opens > closes and opens+closes < n*2:
                dfs(opens, closes+1, string+")")

             
            

        
        dfs(1,0,"(")
        return res

        
            

        