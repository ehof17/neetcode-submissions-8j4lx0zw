"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # keep a mapping of nodes to new nodes?

        if not head:
            return None

        visited = {}
        def clone(node):
            if not node:
                return None
            if node in visited:
                return visited[node]
            copy = Node(node.val)
            visited[node] = copy 
            copy.next = clone(node.next)
            copy.random = clone(node.random)

            return copy

        return clone(head)


