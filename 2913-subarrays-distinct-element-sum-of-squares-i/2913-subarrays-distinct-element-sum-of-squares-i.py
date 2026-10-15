class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        for i in range(n):
            seen = set()
            for j in range(i, n):
                seen.add(nums[j])
                total += len(seen) ** 2
        return total