from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for now, before in prerequisites:
            adj[now].append(before)

        visit = set()
        path = set()
        res = []

        def dfs(i, visit, path, adj):
            if i in path:
                return False
            if i in visit:
                return True

            path.add(i)
            visit.add(i)
            
            for val in adj[i]:
                if not dfs(val, visit, path, adj):
                    return False
            
            path.remove(i)
            res.append(i)


            return True

        for i in range(numCourses):
            if not dfs(i, visit, path, adj):
                return False
        return True
        

        