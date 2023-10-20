class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}

        def inseart(word: str):
            curr = trie
            for x in word:
                curr = curr.setdefault(x, {})
            curr["$"] = word

        for w in words:
            inseart(w)

        m, n = len(board), len(board[0])
        output = []

        def search(curr, r: int, c: int):
            if board[r][c] in curr:
                x = board[r][c]
                board[r][c] = "."
                if word := curr[x].pop("$", None):
                    output.append(word)

                if r > 0:
                    search(curr[x], r - 1, c)
                if r < m - 1:
                    search(curr[x], r + 1, c)
                if c > 0:
                    search(curr[x], r, c - 1)
                if c < n - 1:
                    search(curr[x], r, c + 1)

                board[r][c] = x

        for r in range(m):
            for c in range(n):
                search(trie, r, c)
        return output
