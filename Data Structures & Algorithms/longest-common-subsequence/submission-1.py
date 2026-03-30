class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        maxLen = max(len(text1), len(text2)) 
        cache = [[-1] * maxLen for i in range(maxLen)]
        print(cache)
        
        def helper(s1, s2, i, j, cache):
            if i == len(s1) or j == len(s2):
                return 0

            if cache[i][j] != -1:
                return cache[i][j]
            
            if s1[i] == s2[j]:
                cache[i][j] = 1 + helper(s1, s2, i+1, j+1, cache)
                return cache[i][j]
            
            cache[i][j] = max(
                    helper(s1, s2, i+1, j, cache),
                    helper(s1, s2, i, j+1, cache)
                )
            return cache[i][j]

        return helper(text1, text2, 0,0, cache)
    