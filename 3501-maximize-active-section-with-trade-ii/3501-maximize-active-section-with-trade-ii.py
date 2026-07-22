from typing import List

class SegmentTree:
    def __init__(self, data: List[int]):
        self.n = len(data)
        self.tree = [0] * (2 * self.n)
        for i in range(self.n):
            self.tree[self.n + i] = data[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = max(self.tree[2 * i], self.tree[2 * i + 1])

    def query(self, l: int, r: int) -> int:
        """Returns max in range [l, r] inclusive."""
        if l > r or l < 0 or r >= self.n:
            return 0
        res = 0
        l += self.n
        r += self.n + 1
        while l < r:
            if l & 1:
                res = max(res, self.tree[l])
                l += 1
            if r & 1:
                r -= 1
                res = max(res, self.tree[r])
            l //= 2
            r //= 2
        return res

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        total_ones = s.count('1')

        # 1. Compress consecutive characters into segments: (char, L, R, len)
        segs = []
        seg_id = [0] * n
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            idx = len(segs)
            segs.append((s[i], i, j - 1, j - i))
            for k in range(i, j):
                seg_id[k] = idx
            i = j

        m = len(segs)

        # 2. Precompute full static trade gains for fully internal '1'-segments
        st_data = [0] * m
        for idx in range(1, m - 1):
            if segs[idx][0] == '1' and segs[idx - 1][0] == '0' and segs[idx + 1][0] == '0':
                st_data[idx] = segs[idx - 1][3] + segs[idx + 1][3]

        st = SegmentTree(st_data)

        # Helper to compute exact gain for a specific '1'-segment 'idx' inside range [l, r]
        def calc_gain(idx: int, l: int, r: int) -> int:
            if idx < 1 or idx >= m - 1:
                return 0
            if segs[idx - 1][0] != '0' or segs[idx + 1][0] != '0':
                return 0

            # Compute overlapping zero lengths within range [l, r]
            left_zero = max(0, min(segs[idx - 1][2], r) - max(segs[idx - 1][1], l) + 1)
            right_zero = max(0, min(segs[idx + 1][2], r) - max(segs[idx + 1][1], l) + 1)

            # Trade is valid only if surrounded by '0's on both sides within the query
            if left_zero > 0 and right_zero > 0:
                return left_zero + right_zero
            return 0

        ans = []
        for l, r in queries:
            id_l = seg_id[l]
            id_r = seg_id[r]

            # Find the first '1'-segment fully inside [l, r]
            first_1 = id_l
            while first_1 <= id_r and (segs[first_1][0] != '1' or segs[first_1][1] < l):
                first_1 += 1

            # Find the last '1'-segment fully inside [l, r]
            last_1 = id_r
            while last_1 >= id_l and (segs[last_1][0] != '1' or segs[last_1][2] > r):
                last_1 -= 1

            max_gain = 0
            if first_1 <= last_1:
                # Check boundary '1'-segments with exact overlap calculation
                max_gain = max(max_gain, calc_gain(first_1, l, r))
                max_gain = max(max_gain, calc_gain(last_1, l, r))

                # Query Segment Tree for fully internal '1'-segments
                if first_1 + 1 <= last_1 - 1:
                    max_gain = max(max_gain, st.query(first_1 + 1, last_1 - 1))

            ans.append(total_ones + max_gain)

        return ans