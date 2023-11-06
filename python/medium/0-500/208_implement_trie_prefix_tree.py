class Trie:
    def __init__(self):
        self.root = {"$": False}

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            curr = curr.setdefault(c, {"$": False})
        curr["$"] = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr:
                return False
            curr = curr[c]
        return curr["$"]

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr:
                return False
            curr = curr[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
