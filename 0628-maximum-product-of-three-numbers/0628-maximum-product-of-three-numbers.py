class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        # Option 1: three largest numbers
        candidate1 = nums[-1] * nums[-2] * nums[-3]
        # Option 2: two smallest (could be very negative, product positive) * largest
        candidate2 = nums[0] * nums[1] * nums[-1]
        return max(candidate1, candidate2)