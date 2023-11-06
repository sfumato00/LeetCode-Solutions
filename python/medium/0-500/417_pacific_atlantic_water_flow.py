from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        DIR = [(1, 0), (0, -1), (-1, 0), (0, 1)]
        M, N = len(heights), len(heights[0])

        def dfs(x, y, visited):
            h = heights[x][y]
            visited.add((x, y))
            for dx, dy in DIR:
                x1, y1 = x + dx, y + dy
                if (
                    0 <= x1 < M
                    and 0 <= y1 < N
                    and (x1, y1) not in visited
                    and h <= heights[x1][y1]
                ):
                    dfs(x1, y1, visited)

        pac, atl = set(), set()
        for x in range(M):
            dfs(x, 0, pac)
            dfs(x, N - 1, atl)

        for y in range(N):
            dfs(0, y, pac)
            dfs(M - 1, y, atl)
        ans = []
        for x, row in enumerate(heights):
            for y, _ in enumerate(row):
                if (x, y) in pac and (x, y) in atl:
                    ans += [[x, y]]
        return ans
