class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        ans = -1
        for i in range(n):
            s = 0
            for j in range(i, min(n, i + r)):
                s += nums[j]
                length = j - i + 1
                if length >= l and s > 0:
                    if ans == -1 or s < ans:
                        ans = s
        return ans