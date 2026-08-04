class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        s = set(nums)
        ans = []

        for x in range(min(nums), max(nums) + 1):
            if x not in s:
                ans.append(x)

        return ans