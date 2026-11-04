class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)
        vals = sorted(set(nums))
        m = len(vals)
        rank = {v: i + 1 for i, v in enumerate(vals)}

        cnt = [0] * (m + 1)   # BIT: count of elements
        sm = [0] * (m + 1)    # BIT: sum of elements

        def update(i, dc, dv):
            while i <= m:
                cnt[i] += dc
                sm[i] += dv
                i += i & -i

        def prefix(i):
            c = s = 0
            while i > 0:
                c += cnt[i]
                s += sm[i]
                i -= i & -i
            return c, s

        def kth(kk):  # rank (1-based) of kk-th smallest in window
            pos = 0
            step = 1 << (m.bit_length() - 1)
            while step:
                nxt = pos + step
                if nxt <= m and cnt[nxt] < kk:
                    pos = nxt
                    kk -= cnt[nxt]
                step >>= 1
            return pos + 1

        # Window cost for every start index
        W = [0] * (n - x + 1)
        total = 0
        for i in range(x):
            update(rank[nums[i]], 1, nums[i])
            total += nums[i]

        for i in range(n - x + 1):
            if i > 0:
                out, inn = nums[i - 1], nums[i + x - 1]
                update(rank[out], -1, -out)
                update(rank[inn], 1, inn)
                total += inn - out

            p = kth((x + 1) // 2)      # lower median
            v = vals[p - 1]
            cL, sL = prefix(p)         # elements <= median
            cR = x - cL
            sR = total - sL            # elements > median
            W[i] = v * cL - sL + sR - v * cR

        # DP over prefixes
        INF = float('inf')
        f = [[INF] * (k + 1) for _ in range(n + 1)]
        for j in range(n + 1):
            f[j][0] = 0

        for j in range(1, n + 1):
            for c in range(1, k + 1):
                best = f[j - 1][c]                      # skip element j-1
                if j >= x and f[j - x][c - 1] < INF:    # take window ending at j-1
                    best = min(best, W[j - x] + f[j - x][c - 1])
                f[j][c] = best

        return f[n][k]