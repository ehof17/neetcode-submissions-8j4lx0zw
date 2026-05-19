from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visit = set()
        path = set()
        adj = defaultdict(list)
        res = []
        for now, prev in prerequisites:
            adj[now].append(prev)
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
                return[]
        return res


        
