from typing import List

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def digit_sum(x):
            s = 0
            while x:
                s += x % 10
                x //= 10
            return s

        n = len(nums)
        order = sorted(range(n), key=lambda i: (digit_sum(nums[i]), nums[i]))
        # order[k] = original index of the element that should land at position k
        visited = [False] * n
        swaps = 0

        for start in range(n):
            if visited[start] or order[start] == start:
                continue
            cycle_len = 0
            cur = start
            while not visited[cur]:
                visited[cur] = True
                cur = order[cur]
                cycle_len += 1
            swaps += cycle_len - 1

        return swaps