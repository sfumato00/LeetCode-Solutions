from collections import defaultdict
from typing import List


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        M, N = len(grid), len(grid[0])

        def dfs(r, c, label):
            if 0 <= r < M and 0 <= c < N and grid[r][c] == 1:
                ret = 1
                grid[r][c] = label
                for dr, dc in dirs:
                    ret += dfs(r + dr, c + dc, label)
                return ret
            return 0

        areas = defaultdict(int)
        label = 2
        for x in range(M):
            for y in range(N):
                if grid[x][y] == 1:
                    areas[label] = dfs(x, y, label)
                    label += 1

        if len(areas) <= 1:
            return areas[label - 1] + 1 if M * N > areas[label - 1] else M * N

        ans = 0
        label_set = set()
        for x in range(M):
            for y in range(N):
                if grid[x][y] != 0:
                    continue

                for dx, dy in dirs:
                    x1, y1 = x + dx, y + dy
                    if 0 <= x1 < M and 0 <= y1 < N:
                        label_set.add(grid[x1][y1])

                ans = max(ans, sum([areas[l] for l in label_set]) + 1)
                label_set.clear()

        return ans
