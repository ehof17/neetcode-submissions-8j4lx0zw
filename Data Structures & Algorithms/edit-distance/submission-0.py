class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        maxLen = max(len(word1), len(word2))
        cache = [[-1] * maxLen for i in range(maxLen)]

        def helper(i, j, s1, s2, cache):
            if len(s1) == i:
                return len(s2)-j
            if len(s2) == j:
                return len(s1)-i

            if cache[i][j] != -1:
                return cache[i][j]

            if s1[i] == s2[j]:
                cache[i][j] = helper(i+1,j+1, s1,s2, cache)
                return cache[i][j]
            
            val = min(
                helper(i,j+1, s1,s2, cache),
                helper(i+1,j, s1,s2, cache),
                

            )
            val = min (
                val,
                helper(i+1,j+1, s1,s2, cache)
            )
            cache[i][j] = val + 1
            return cache[i][j]

        return helper(0,0,word1,word2,cache)
        


            

            
            

            
            