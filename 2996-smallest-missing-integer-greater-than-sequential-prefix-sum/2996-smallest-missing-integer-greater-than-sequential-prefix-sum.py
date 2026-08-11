class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        n = len(nums)
        # Find length of longest sequential prefix
        i = 1
        while i < n and nums[i] == nums[i - 1] + 1:
            i += 1
        
        total = sum(nums[:i])
        
        seen = set(nums)
        while total in seen:
            total += 1
        
        return total