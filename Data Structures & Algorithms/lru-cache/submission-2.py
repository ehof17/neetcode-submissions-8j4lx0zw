class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left
        
    
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    # inserts at the top
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev
    


    def get(self, key: int) -> int:
        # need to bubble it up\?\
        # Can search for it
        # then after we get this val
        # we need to set to top of cache
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1
       

    def put(self, key: int, value: int) -> None:
        # holup
        # if this is diff
        # cache wouldn't change length
        need_remove = len(self.cache) == self.cap
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.cache[key]=node
            self.remove(node)
            self.insert(node)
            return
        else:
            self.cache[key] = Node(key, value)
            self.insert(self.cache[key])

        if need_remove:
            self.cache.pop(self.left.next.key)
            self.remove(self.left.next)

       
        # remove self.left.next?
        # need to put it at the back

