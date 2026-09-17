from typing import List

class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        dp = [float('inf')] * n  # dp[i] = min length subarray with sum=target ending at or before i
        ans = float('inf')
        left = 0
        window_sum = 0

        for right in range(n):
            window_sum += arr[right]

            while window_sum > target:
                window_sum -= arr[left]
                left += 1

            # carry forward previous best
            dp[right] = dp[right - 1] if right > 0 else float('inf')

            if window_sum == target:
                curr_len = right - left + 1
                if left > 0 and dp[left - 1] != float('inf'):
                    ans = min(ans, dp[left - 1] + curr_len)
                dp[right] = min(dp[right], curr_len)

        return ans if ans != float('inf') else -1