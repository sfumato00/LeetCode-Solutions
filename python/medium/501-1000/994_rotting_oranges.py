from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        rows, cols = len(grid), len(grid[0])
        q = deque([(r, c) for r in range(rows) for c in range(cols) if grid[r][c] == 2])
        time = 0
        while q:
            k = len(q)
            for _ in range(k):
                r, c = q.popleft()
                for dr, dc in dirs:
                    r1, c1 = r + dr, c + dc
                    if 0 <= r1 < rows and 0 <= c1 < cols and grid[r1][c1] == 1:
                        grid[r1][c1] = 2
                        q += [(r1, c1)]
            time += 1 if q else 0

        if any(1 in row for row in grid):
            return -1
        return time
