class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        lens = len(strs)
        i = 0
        while i < 200:
            curSet = set()
            for word in strs:
                if i >= len(word):
                    return res
                # word[i]
                curSet.add(word[i])

                if len(curSet)>1:
                    return res
            res += strs[0][i]
            i+=1
    

        return res