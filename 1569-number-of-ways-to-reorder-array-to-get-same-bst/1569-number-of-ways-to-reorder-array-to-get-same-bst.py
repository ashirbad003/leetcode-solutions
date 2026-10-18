from typing import List

MOD = 10**9 + 7

class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        n = len(nums)
        # Pascal's triangle for binomial coefficients mod MOD
        C = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            C[i][0] = 1
            for j in range(1, i + 1):
                C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % MOD

        def ways(arr):
            if len(arr) <= 2:
                return 1
            root = arr[0]
            left = [x for x in arr if x < root]
            right = [x for x in arr if x > root]
            L, R = len(left), len(right)
            return C[L + R][L] * ways(left) % MOD * ways(right) % MOD

        return (ways(nums) - 1) % MOD