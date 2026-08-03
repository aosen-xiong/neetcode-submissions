class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        max_area = 0

        def dfs(r, c):
            # Base Case: Out of bounds or water (0)
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0:
                return 0

            # Mark cell as visited by sinking it to 0
            grid[r][c] = 0

            # Current cell (1) + total area from all 4 directions
            return 1 + (
                dfs(r + 1, c) +
                dfs(r - 1, c) +
                dfs(r, c + 1) +
                dfs(r, c - 1)
            )

        # Outer Loop: Traverse the grid
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r, c))

        return max_area