from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        DIR = [0, 1, 0, -1, 0]

        def dfs(r, c):
            nonlocal grid
            ret = 0
            if 0 <= r < R and 0 <= c < C and grid[r][c] == 1:
                ret = 1
                grid[r][c] = 0
                for d in range(4):
                    rr, cc = r + DIR[d], c + DIR[d + 1]
                    ret += dfs(rr, cc)
            return ret

        ans = 0
        for r, row in enumerate(grid):
            for c, v in enumerate(row):
                if v == 1:
                    ans = max(ans, dfs(r, c))
        return ans
