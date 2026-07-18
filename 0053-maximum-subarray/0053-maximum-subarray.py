class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = ans = nums[0]

        for i in range(1, len(nums)):
            curr = max(nums[i], curr + nums[i])
            ans = max(ans, curr)

        return ans