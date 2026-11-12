class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        best = inc = dec = 1
        for i in range(1, len(nums)):
            inc = inc + 1 if nums[i] > nums[i-1] else 1
            dec = dec + 1 if nums[i] < nums[i-1] else 1
            best = max(best, inc, dec)
        return best