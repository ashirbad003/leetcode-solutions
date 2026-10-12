class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7

        # count[b] = how many numbers have bit b set
        count = [0] * 31
        for num in nums:
            for b in range(31):
                if num >> b & 1:
                    count[b] += 1

        total = 0
        for _ in range(k):
            x = 0
            for b in range(31):
                if count[b] > 0:
                    x |= 1 << b
                    count[b] -= 1
            total = (total + x * x) % MOD

        return total