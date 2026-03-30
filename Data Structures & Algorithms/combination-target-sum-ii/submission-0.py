class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        # i, 
        cache = []

        def dfs(i, curSet, resSet, target):
            if i >= len(candidates):
                if target == 0:
                    if curSet not in resSet:
                        resSet.append(curSet.copy())
                return

            
            curSet.append(candidates[i])
            dfs(i+1, curSet, resSet, target-candidates[i])
            curSet.pop()

            dfs(i+1, curSet, resSet, target)
             

        curSet = []
        resSet = []
        dfs(0, curSet, resSet, target)
        return resSet

            
    