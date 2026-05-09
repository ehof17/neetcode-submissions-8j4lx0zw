class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        i = 0
        resSet = []
        def dfs(i, curSet, curVal):
            if curVal > target:return
            if curVal == target:
                resSet.append(curSet.copy())
                return
            if i >= len(candidates):
                return

            # try do dfs with the new number
            curSet.append(candidates[i])
            curVal+=candidates[i]

            dfs(i+1,curSet, curVal)
            val_at_i = curSet.pop()
            # do a dfs without new number
            i+=1
            while i < len(candidates) and candidates[i]==val_at_i:
                i+=1
            curVal-=val_at_i
            dfs(i,curSet, curVal)
        
        dfs(0, [],0)
        return resSet