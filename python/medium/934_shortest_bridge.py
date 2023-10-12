from collections import deque
from typing import List


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = set()
        dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]

        def label_first_island():
            def dfs(r, c):
                if 0 <= r < m and 0 <= c < n and grid[r][c] == 1:
                    grid[r][c] = 2
                    visited.add((r, c))
                    for dr, dc in dirs:
                        dfs(r + dr, c + dc)

            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1:
                        dfs(i, j)
                        return

        label_first_island()
        q = deque(list(visited))
        steps = 0
        while q:
            n_level = len(q)
            for _ in range(n_level):
                r, c = q.popleft()
                for dr, dc in dirs:
                    rr, cc = r + dr, c + dc
                    if rr < 0 or rr == m or cc < 0 or cc >= n:
                        continue

                    if grid[rr][cc] == 1:
                        return steps

                    if grid[rr][cc] == 0 and (rr, cc) not in visited:
                        visited.add((rr, cc))
                        q.append((rr, cc))
            steps += 1
        return -1
