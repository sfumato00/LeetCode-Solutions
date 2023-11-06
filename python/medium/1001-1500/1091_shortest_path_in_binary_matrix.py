"""LeetCode 1091. Shortest Path in Binary Matrix."""
from collections import deque
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] or grid[-1][-1]:
            return -1

        dirs = [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]
        n = len(grid)
        grid[0][0] = 1
        q = deque([(0, 0)])
        path = 0
        while q:
            path += 1
            level_n = len(q)
            for _ in range(level_n):
                r, c = q.popleft()
                if r == n - 1 and c == n - 1:
                    return path
                for dr, dc in dirs:
                    rr, cc = r + dr, c + dc
                    if 0 <= rr < n and 0 <= cc < n and not grid[rr][cc]:
                        grid[rr][cc] = 1
                        q.append((rr, cc))
        return -1
