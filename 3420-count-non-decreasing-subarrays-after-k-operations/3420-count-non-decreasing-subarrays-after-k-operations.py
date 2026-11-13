from typing import List

class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)

        # prefix sums of nums
        P = [0] * (n + 1)
        for i, x in enumerate(nums):
            P[i + 1] = P[i] + x

        # nge[i] = next index with value strictly greater than nums[i] (or n)
        nge = [n] * n
        st = []
        for i in range(n):
            while st and nums[st[-1]] < nums[i]:
                nge[st.pop()] = i
            st.append(i)

        # C[i] = cost to make nums[i..n-1] non-decreasing, with prefix max starting at i
        C = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            e = nge[i]
            C[i] = nums[i] * (e - i) - (P[e] - P[i]) + C[e]

        # binary lifting over the nge chain
        LOG = max(1, n.bit_length())
        up = [nge + [n]]
        for _ in range(1, LOG):
            prev = up[-1]
            up.append([prev[prev[i]] for i in range(n + 1)])

        def cost(l: int, r: int) -> int:
            # find chain node p (p <= r < nge[p]) that is the prefix max position for r
            p = l
            for t in range(LOG - 1, -1, -1):
                q = up[t][p]
                if q <= r:
                    p = q
            # cost of [l, p) + cost of [p, r] where max is nums[p]
            return (C[l] - C[p]) + nums[p] * (r - p + 1) - (P[r + 1] - P[p])

        ans = 0
        r = 0
        for l in range(n):
            if r < l:
                r = l
            while r + 1 < n and cost(l, r + 1) <= k:
                r += 1
            ans += r - l + 1
        return ans