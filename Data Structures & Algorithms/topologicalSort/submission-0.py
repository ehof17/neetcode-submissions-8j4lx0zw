from collections import defaultdict
class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
        
        # First we want to add all the descendants
        start = 0
        res = []
        adj[start]
        saw = set()
        path = set()

        def dfs(val, adj, visit, res, path):
            if val in path:
                return False
            if val in saw:
                return True

            saw.add(val)
            path.add(val)
            # look at neighbors first
            for val2 in adj[val]:
                if not dfs(val2, adj, visit, res, path):
                    return False
            path.remove(val)
            res.append(val)
            return True

        # look at node
        for i in range(n):
            val = dfs(i, adj, saw, res, path)
            if val == False:
                return []
        return res[::-1]

    