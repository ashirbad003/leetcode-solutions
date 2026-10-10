class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        k = k1 + k2
        d = [abs(a - b) for a, b in zip(nums1, nums2)]

        # Cost to bring every difference down to at most x
        def cost(x: int) -> int:
            return sum(v - x for v in d if v > x)

        # Smallest x such that cost(x) <= k
        lo, hi = 0, max(d)
        while lo < hi:
            mid = (lo + hi) // 2
            if cost(mid) <= k:
                hi = mid
            else:
                lo = mid + 1
        x = lo

        if x == 0:
            return 0

        rem = k - cost(x)  # leftover operations
        total = 0
        for v in d:
            c = min(v, x)
            total += c * c
        # Use leftover ops to drop some elements equal to x down to x-1
        total -= rem * (2 * x - 1)
        return total