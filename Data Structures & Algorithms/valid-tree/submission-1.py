from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # invalid if there are cycles
        # how to tell if there cycles
        # If we visit a node again from a path other than its parent
        # we have a cycle
        visited = set()
        if len(edges) > (n-1):
            return False
        adj = defaultdict(list)
        for node in edges:
            src, dst = node
            adj[src].append(dst)
            adj[dst].append(src)
        
        def dfs(node, parent):
            if node in visited: return False

            visited.add(node)
            for neighbor in adj[node]:
                if neighbor == parent:
                    continue
                if not dfs(neighbor, node):
                    return False
            return True

        return dfs(0, -1) and n == len(visited)     
