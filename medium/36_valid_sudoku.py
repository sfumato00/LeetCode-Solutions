from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        Rows = [[False] * 9 for _ in range(9)]
        Cols = [[False] * 9 for _ in range(9)]
        Blocks = [[False] * 9 for _ in range(9)]

        for r, row in enumerate(board):
            for c, x in enumerate(row):
                if x == ".":
                    continue

                k = int(x) - 1
                if Rows[r][k] or Cols[c][k] or Blocks[(r // 3) * 3 + c // 3][k]:
                    return False

                Rows[r][k] = True
                Cols[c][k] = True
                Blocks[(r // 3) * 3 + c // 3][k] = True
        return True
