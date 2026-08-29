class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        indexed = sorted(range(n), key=lambda i: nums[i])
        result = [0] * n
        i = 0
        while i < n:
            j = i
            while j + 1 < n and nums[indexed[j + 1]] - nums[indexed[j]] <= limit:
                j += 1
            group_indices = sorted(indexed[i:j+1])
            group_values = [nums[indexed[k]] for k in range(i, j + 1)]
            for pos, val in zip(group_indices, group_values):
                result[pos] = val
            i = j + 1
        return result