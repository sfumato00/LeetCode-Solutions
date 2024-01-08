import heapq
from math import inf
from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        DIR = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        hp = [(grid[0][0], 0, 0)]
        time = {(0, 0): 0}
        n = len(grid)
        while hp:
            t, x, y = heapq.heappop(hp)
            if x == n - 1 and y == n - 1:
                return t

            for dx, dy in DIR:
                _x, _y = x + dx, y + dy
                if (
                    0 <= _x < n
                    and 0 <= _y < n
                    and grid[_x][_y] < time.get((_x, _y), inf)
                ):
                    time[(_x, _y)] = grid[_x][_y]
                    heapq.heappush(hp, (max(grid[_x][_y], t), _x, _y))

        return -1
