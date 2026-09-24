class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i, n in enumerate(nums):
            s = 0
            while n:
                s += n % 10
                n //= 10
            if s == i:
                return i
        return -1