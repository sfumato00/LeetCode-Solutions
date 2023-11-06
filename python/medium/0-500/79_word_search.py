from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]
        _m, _c, k = len(board), len(board[0]), len(word)

        def exist(row, col, i):
            if i == k:
                return True

            if 0 <= row < _m and 0 <= col < _c and board[row][col] == word[i]:
                temp = board[row][col]
                board[row][col] = ""
                for d_r, d_c in directions:
                    if exist(row + d_r, col + d_c, i + 1):
                        return True
                board[row][col] = temp
            return False

        for _r, row in enumerate(board):
            for _c, _ in enumerate(row):
                if exist(_r, _c, 0):
                    return True
        return False
