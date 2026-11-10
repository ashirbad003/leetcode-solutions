class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        # dp[i] = minimum cost to reach step i
        # costs is 1-indexed in the problem, so step i's cost is costs[i-1]
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            best = float('inf')
            for j in range(max(0, i - 3), i):
                best = min(best, dp[j] + costs[i - 1] + (i - j) ** 2)
            dp[i] = best
        return dp[n]