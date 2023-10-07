class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]
        visited = set()
        ans = 0

        def dfs(r, c):
            nonlocal ans
            if (r, c) in visited:
                return 0

            ret = 0
            if 0 <= r < m and 0 <= c < n and grid[r][c] == 1:
                visited.add((r, c))
                for dr, dc in dirs:
                    ret += dfs(r + dr, c + dc)
                return ret
            else:
                return 1

        for r, row in enumerate(grid):
            for c, x in enumerate(row):
                if x == 1:
                    return dfs(r, c)
        return 0
