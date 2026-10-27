class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid = [['#'] * n for _ in range(m)]
        for j in range(n):
            grid[0][j] = '.'      # top row free
        for i in range(m):
            grid[i][n - 1] = '.'  # last column free
        return [''.join(row) for row in grid]