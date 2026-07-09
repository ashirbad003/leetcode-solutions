class Solution:
    def twoSum(self, nums, target):
        mp = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in mp:
                return [mp[diff], i]
            mp[num] = i