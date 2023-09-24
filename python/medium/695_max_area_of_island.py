from typing import List


class Solution:
    """Class to solve the maximum area of island problem."""

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        Determines the maximum area of an island in the grid.

        Parameters:
        - grid: List of lists representing the grid.

        Returns:
        - int: Maximum area of the island.
        """
        if not grid or not grid[0]:
            return 0

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        rows, cols = len(grid), len(grid[0])

        def depth_first_search(row: int, col: int) -> int:
            """
            Perform a depth-first search starting from a land cell.

            Parameters:
            - row: Starting row index.
            - col: Starting column index.

            Returns:
            - int: Count of cells in the current island.
            """
            if 0 <= row < rows and 0 <= col < cols and grid[row][col] == 1:
                grid[row][col] = 0
                area = 1
                for delta_row, delta_col in directions:
                    area += depth_first_search(row + delta_row, col + delta_col)
                return area
            return 0

        max_area = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    max_area = max(max_area, depth_first_search(row, col))

        return max_area
