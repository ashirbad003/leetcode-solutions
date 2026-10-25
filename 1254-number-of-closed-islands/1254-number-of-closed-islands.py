class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            # out of bounds ya water (1) ya already visited -> stop
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != 0:
                return
            grid[r][c] = 1  # visited, ise water bana do
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # Step 1: border se connected land ko hata do (ye closed nahi ho sakte)
        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols - 1)
        for c in range(cols):
            dfs(0, c)
            dfs(rows - 1, c)

        # Step 2: bache hue land components gino
        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    count += 1
                    dfs(r, c)

        return count