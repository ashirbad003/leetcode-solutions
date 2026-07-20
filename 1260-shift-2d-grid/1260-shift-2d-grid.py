class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        total = m * n
        k %= total

        # Flatten the grid
        arr = []
        for row in grid:
            arr.extend(row)

        # Right rotate by k
        arr = arr[-k:] + arr[:-k]

        # Convert back to 2D grid
        ans = []
        idx = 0
        for i in range(m):
            ans.append(arr[idx:idx + n])
            idx += n

        return ans