from typing import List

MOD = 10**9 + 7

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        size = 4 * n
        s1 = [0] * size   # sum of distinct counts
        s2 = [0] * size   # sum of squares of distinct counts
        lz = [0] * size

        def apply(node, length, v):
            s2[node] += 2 * v * s1[node] + length * v * v
            s1[node] += length * v
            lz[node] += v

        def push(node, l, r):
            if lz[node]:
                mid = (l + r) // 2
                apply(2 * node, mid - l + 1, lz[node])
                apply(2 * node + 1, r - mid, lz[node])
                lz[node] = 0

        def update(node, l, r, ql, qr, v):
            if qr < l or r < ql:
                return
            if ql <= l and r <= qr:
                apply(node, r - l + 1, v)
                return
            push(node, l, r)
            mid = (l + r) // 2
            update(2 * node, l, mid, ql, qr, v)
            update(2 * node + 1, mid + 1, r, ql, qr, v)
            s1[node] = s1[2 * node] + s1[2 * node + 1]
            s2[node] = s2[2 * node] + s2[2 * node + 1]

        def query(node, l, r, ql, qr):
            if qr < l or r < ql:
                return 0
            if ql <= l and r <= qr:
                return s2[node]
            push(node, l, r)
            mid = (l + r) // 2
            return query(2 * node, l, mid, ql, qr) + query(2 * node + 1, mid + 1, r, ql, qr)

        last = {}
        total = 0
        for r in range(n):
            x = nums[r]
            prev = last.get(x, -1)
            # distinct count +1 for left endpoints in (prev, r]
            update(1, 0, n - 1, prev + 1, r, 1)
            last[x] = r
            # sum of squares over all left endpoints 0..r
            total = (total + query(1, 0, n - 1, 0, r)) % MOD

        return total