class Solution:
    def leftmostBuildingQueries(self, heights: list[int], queries: list[list[int]]) -> list[int]:
        n = len(heights)
        size = 1
        while size < n:
            size *= 2

        # max segment tree
        tree = [0] * (2 * size)
        for i, h in enumerate(heights):
            tree[size + i] = h
        for i in range(size - 1, 0, -1):
            tree[i] = max(tree[2 * i], tree[2 * i + 1])

        def first_greater(start, target):
            # start ya uske right me sabse left index jiski height > target, warna -1
            def go(node, lo, hi):
                if hi < start or tree[node] <= target:
                    return -1
                if lo == hi:
                    return lo
                mid = (lo + hi) // 2
                res = go(2 * node, lo, mid)
                if res != -1:
                    return res
                return go(2 * node + 1, mid + 1, hi)
            return go(1, 0, size - 1)

        ans = []
        for a, b in queries:
            if a > b:
                a, b = b, a
            if a == b or heights[a] < heights[b]:
                ans.append(b)
                continue
            idx = first_greater(b + 1, max(heights[a], heights[b]))
            ans.append(idx if idx != -1 and idx < n else -1)

        return ans