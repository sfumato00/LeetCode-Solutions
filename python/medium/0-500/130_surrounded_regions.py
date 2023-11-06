from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return

        DIR = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        R, C = len(board), len(board[0])

        def dfs(r: int, c: int) -> None:
            if 0 <= r < R and 0 <= c < C and board[r][c] == "O":
                board[r][c] = "+"
                for dr, dc in DIR:
                    dfs(r + dr, c + dc)

        # Mark 'O's on the border and their reachable 'O's with '+'
        for i in range(R):
            dfs(i, 0)
            dfs(i, C - 1)
        for j in range(C):
            dfs(0, j)
            dfs(R - 1, j)

        # Flip 'O's to 'X's and '+' back to 'O'
        for r in range(R):
            for c in range(C):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "+":
                    board[r][c] = "O"
