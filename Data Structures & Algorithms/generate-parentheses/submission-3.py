class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return ["()"]

        res = []
        def dfs(opens, closes, cur):
            # allowed pairs n opens, n closes
            sz = len(cur)
            if sz == 2*n:
                res.append(cur)
                return
            
            # if we can add an opening
            if opens < n:
                dfs(opens+1, closes, cur+"(")

            # if we can add a closing
            if opens > closes < n:
                dfs(opens, closes+1, cur+")")

            
        dfs(1, 0, "(")
    

    
        return res

        
            

        