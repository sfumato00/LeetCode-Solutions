from typing import List


class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        sums = [[0] * (n + 1) for _ in range(m + 1)]
        for r, row in enumerate(matrix):
            for c, x in enumerate(row):
                sums[r + 1][c + 1] = (
                    matrix[r][c] + sums[r][c + 1] + sums[r + 1][c] - sums[r][c]
                )
        self.sums = sums

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sums = self.sums
        return (
            sums[row2 + 1][col2 + 1]
            - sums[row1][col2 + 1]
            - sums[row2 + 1][col1]
            + sums[row1][col1]
        )


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
