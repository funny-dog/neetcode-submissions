class WordDictionary:

    def __init__(self):
        self.children = {}
        self.is_end = False

    def addWord(self, word: str) -> None:
        node = self
        for c in word:
            if c not in node.children:
                node.children[c] = WordDictionary()
            node = node.children[c]
        node.is_end = True

    def search(self, word: str) -> bool:
        def dfs(node, index):
            if index >= len(word):
                return node.is_end
            c = word[index]
            if c not in node.children and c != ".":
                return False
            if c == ".":
                for child in node.children.values():
                    if dfs(child, index + 1):
                        return True
                return False
            else:
                return dfs(node.children[c], index + 1)
        return dfs(self, 0)