from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R, C = len(grid), len(grid[0])
        DIR = [1, 0, -1, 0, 1]

        def dfs(r, c):
            if 0 <= r < R and 0 <= c < C and grid[r][c] == "1":
                grid[r][c] = "0"
                for d in range(4):
                    dfs(r + DIR[d], c + DIR[d + 1])

        count = 0
        for r, row in enumerate(grid):
            for c, x in enumerate(row):
                if x == "1":
                    count += 1
                    dfs(r, c)

        return count
