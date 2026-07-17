from typing import List
from bisect import bisect_right

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        mx = max(nums)

        freq = [0] * (mx + 1)
        for x in nums:
            freq[x] += 1

        # cnt[d] = numbers divisible by d
        cnt = [0] * (mx + 1)
        for d in range(1, mx + 1):
            for j in range(d, mx + 1, d):
                cnt[d] += freq[j]

        # exact[d] = pairs whose gcd is exactly d
        exact = [0] * (mx + 1)
        for d in range(mx, 0, -1):
            c = cnt[d]
            pairs = c * (c - 1) // 2
            for j in range(2 * d, mx + 1, d):
                pairs -= exact[j]
            exact[d] = pairs

        values = []
        prefix = []

        s = 0
        for g in range(1, mx + 1):
            if exact[g]:
                values.append(g)
                s += exact[g]
                prefix.append(s)

        ans = []
        for q in queries:
            idx = bisect_right(prefix, q)
            ans.append(values[idx])

        return ans