class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        i = 0
        # let it be the first one once
        num = candidates[i]
        # Add all things of L and or R that add up
        L = i+1
        resSet=[]
        def dfs(i, curSet, total):
            if total == target:
                resSet.append(curSet.copy())
                return
            if total > target or i == len(candidates):
                return
    
            curSet.append(candidates[i])
            dfs(i+1, curSet, total+candidates[i])
            curSet.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
            dfs(i+1, curSet, total)
        curSet=[]
        dfs(0, curSet, 0)
        return resSet

        # then increment i to the next on



            
    