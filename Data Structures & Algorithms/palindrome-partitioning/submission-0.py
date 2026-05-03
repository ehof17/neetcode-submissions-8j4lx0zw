class Solution:
 
    def is_pal(self, word):
        l = 0
        r = len(word)-1
        # wow
        # woow
        # 
        while l <= r:
            if word[l]!=word[r]:
                return False
            l+=1
            r-=1
        return True

    def partition(self, s: str) -> List[List[str]]:
        # start + 0 more letter
        # start + 1 more letter
        # start+1 + 0 more letter
        # start
        res = []
        # well we know that all chars will be one list
        # aab -> "a","a","b"
        self.res = []
        # 
        i = 0
        j = 0

        # need to get every single way we can partition 
        # aab
        # a or aa or aab
        # pal. pal.  not pal. not gonna continue
        # a (ab) is remaining lets try and partition them
        # a 
        # just take first character as one parition
        # take first 2 characters
        # take entire string as first parition
        part = []
        def dfs(i):
            if i >=len(s):
                res.append(part.copy())
                return
            for j in range(i, len(s)):
                if self.is_pal(s[i:j+1]):
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()
        dfs(0)
        return res
        
        