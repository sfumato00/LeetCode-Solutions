class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n, m = len(grid), len(grid[0])
        p = [[0] * m for _ in range(n)]
        prod = 1
        for r, row in enumerate(grid):
            for c, x in enumerate(row):
                p[r][c] = prod
                prod *= x
                prod %= 12345

        prod = 1
        for r in range(n - 1, -1, -1):
            for c in range(m - 1, -1, -1):
                p[r][c] *= prod
                p[r][c] %= 12345
                prod *= grid[r][c]
                prod %= 12345
        return p
