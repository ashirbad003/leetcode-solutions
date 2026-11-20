from collections import defaultdict

class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()
        f = defaultdict(int)
        for x in nums:
            f[x + 1] = max(f[x + 1], f[x] + 1)
            f[x] = max(f[x], f[x - 1] + 1)
        return max(f.values())