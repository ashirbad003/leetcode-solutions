class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        rows = [sum(row) for row in grid]
        cols = [sum(col) for col in zip(*grid)]

        count = 0
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if val and (rows[i] > 1 or cols[j] > 1):
                    count += 1
        return count