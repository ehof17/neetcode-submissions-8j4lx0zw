class TreeNode:
    def __init__(self):
        self.word = False
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.root = TreeNode()
        

    def addWord(self, word: str) -> None:
        node = self.root
        i = 0
        while i < len(word):
            char = word[i]
            if not node.children.get(char):
                node.children[char]=TreeNode()
            node = node.children[char]
            i+=1
        node.word = True
        
    def search(self, word: str):
        node = self.root
        i = 0
        def dfs(node, j):
            if not node:
                return False
            if j == len(word):
                return node.word
            char = word[j]
            if char == ".":
                
                for key, child in node.children.items():
                    if dfs(child, j+1): return True
                
                return False

            else:
                if char not in node.children: return False
                node = node.children[char]
                return dfs(node, j+1)
        return dfs(self.root, 0)
       
       