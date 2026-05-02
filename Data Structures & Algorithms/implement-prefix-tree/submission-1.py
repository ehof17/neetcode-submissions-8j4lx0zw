class TreeNode():
    def __init__(self):
        self.children = {}
        self.word = False

class PrefixTree:

    def __init__(self):
        self.root = TreeNode()
        

    def insert(self, word: str) -> None:
        node = self.root
        i = 0
        while i < len(word):
            char = word[i]
            if char in node.children:
                node = node.children[char]
            else:
                node.children[char] = TreeNode()
                node = node.children[char]
            i+=1
        node.word=True
        print(node)
      
        
       


    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            if c in node.children:
                node = node.children[c]
            else: return False
        return node.word

        
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            if c in node.children:
                node = node.children[c]
            else: return False
        return True

        
        
        