class TreeNode:
    def __init__(self):
        self.word = False
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.root = TreeNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TreeNode()
            curr = curr.children[c]
        curr.word = True

    def search(self, word: str):
        curr = self.root
        def dfs(j, root):
            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in root.children.values():
                        #skip the .
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    if c not in root.children:
                        return False
                    root = root.children[c]
                
            return root.word
        return dfs(0, curr)
            


     