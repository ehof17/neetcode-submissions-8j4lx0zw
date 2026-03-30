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
        def dfs(op, clos, curr):
            # if op == clos == n: return
            if op == clos == n:
                res.append(curr)
                return


            # if we have more opens than closes
            # we can close it
            if op > clos:
                dfs(op, clos+1, curr+")")
            

            # if we have fewer opens than available
            if op < n:
                dfs(op+1, clos, curr+"(")




        
        dfs(1,0,"(")
        return res

        
            

        