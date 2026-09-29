class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])

        if (m + n - 1) % 2 != 0 or grid[0][0] == ')' or grid[m-1][n-1] == '(':
            return False

        # dp[j] = set of possible "open - close" balances reachable at current row, col j
        dp = [set() for _ in range(n)]
        dp[0].add(1)  # grid[0][0] is '('

        for j in range(1, n):
            if not dp[j-1]:
                break
            delta = 1 if grid[0][j] == '(' else -1
            for b in dp[j-1]:
                nb = b + delta
                if nb >= 0:
                    dp[j].add(nb)

        for i in range(1, m):
            new_dp = [set() for _ in range(n)]
            delta = 1 if grid[i][0] == '(' else -1
            for b in dp[0]:
                nb = b + delta
                if nb >= 0:
                    new_dp[0].add(nb)

            for j in range(1, n):
                delta = 1 if grid[i][j] == '(' else -1
                for b in dp[j] | new_dp[j-1]:
                    nb = b + delta
                    if nb >= 0:
                        new_dp[j].add(nb)

            dp = new_dp

        return 0 in dp[n-1]