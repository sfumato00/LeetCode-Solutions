class WordDictionary:
    def __init__(self):
        self.root = {"$": False}

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr:
                curr[c] = {"$": False}
            curr = curr[c]
        curr["$"] = True

    def search(self, word: str) -> bool:
        n = len(word)

        def dfs(curr, pos):
            if pos == n:
                return curr["$"]

            c = word[pos]
            if c != ".":
                return c in curr and dfs(curr[c], pos + 1)

            for k in curr:
                if k == "$":
                    continue

                if dfs(curr[k], pos + 1):
                    return True
            return False

        return dfs(self.root, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
